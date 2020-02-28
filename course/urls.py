# -*- utf-8 -*-
from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView, \
    CreateLessonView, ListLessonView, DetailLessonView, StudentListLessonView

app_name = 'course'
urlpatterns = [
    # path('about/', TemplateView.as_view(template_name='course/about.html')),
    path('about/', AboutView.as_view(), name='about'),
    path('course-list/', CourseListView.as_view(), name='course_list'),
    path('manage-course/', ManageCourseListView.as_view(), name='manage_course'),
    path('create-course/', CreateCourseView.as_view(), name='create_course'),
    re_path(r'delete-course/(?P<pk>\d+)/$', DeleteCourseView.as_view(), name='delete_course'),
    path('create-lesson/', CreateLessonView.as_view(), name='create_lesson'),
    re_path(r'list-lessons/(?P<course_id>\d+)/$', ListLessonView.as_view(), name='list_lessons'),
    re_path(r'detail-lesson/(?P<lesson_id>\d+)/$', DetailLessonView.as_view(), name='detail_lesson'),
    re_path(r'lessons-list/(?P<course_id>\d+)/$', StudentListLessonView.as_view(), name='lessons_list'),
]
