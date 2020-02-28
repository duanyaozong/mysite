# coding:utf8
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from .forms import CreateCourseForm, CreateLessonForm
from .models import Course, Lesson

import json


class AboutView(TemplateView):
    template_name = 'course/about.html'


class CourseListView(ListView):
    model = Course  # Course.objects.all()
    # queryset = Course.objects.filter(user=User.objects.filter(username='laowang'))
    context_object_name = 'courses'  # 传入模板中的变量名称
    template_name = 'course/course_list.html'


class UserMixin:
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)


class UserCourseMixin(UserMixin, LoginRequiredMixin):
    model = Course
    login_url = '/account/login/'


class ManageCourseListView(UserCourseMixin, ListView):  # 课程管理
    context_object_name = 'courses'
    template_name = 'course/manage/manage_course_list.html'


class CreateCourseView(UserCourseMixin, CreateView):  # 继承CreateView不需要写get（）方法
    fields = ['title', 'overview']
    template_name = 'course/manage/create_course.html'

    def post(self, request, *args, **kwargs):
        form = CreateCourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect('course:manage_course')
        return self.render_to_response({'form': form})  # 省去了request


class DeleteCourseView(UserCourseMixin, DeleteView):
    # template_name = 'course/manage/delete_course_confirm.html'
    success_url = reverse_lazy('course:manage_course')

    def dispatch(self, *args, **kwargs):
        resp = super(DeleteCourseView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            return resp


class CreateLessonView(LoginRequiredMixin, View):
    model = Lesson
    login_url = '/account/login/'

    def get(self, request, *args, **kwargs):
        form = CreateLessonForm(user=self.request.user)
        return render(request, 'course/manage/create_lesson.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = CreateLessonForm(self.request.user, request.POST, request.FILES)
        if form.is_valid():
            new_lesson = form.save(commit=False)
            new_lesson.user = self.request.user
            new_lesson.save()
            return redirect('course:manage_course')


class ListLessonView(LoginRequiredMixin, TemplateResponseMixin, View):
    login_url = '/account/login/'
    template_name = 'course/manage/list_lessons.html'

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        return self.render_to_response({'course': course})


class DetailLessonView(LoginRequiredMixin, TemplateResponseMixin, View):
    login_url = '/account/login/'
    template_name = 'course/manage/detail_lesson.html'

    def get(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        return self.render_to_response({'lesson': lesson})


class StudentListLessonView(ListLessonView):
    template_name = 'course/slist_lessons.html'

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs['course_id'])
        course.student.add(self.request.user)
        return HttpResponse('ok')