# -*- utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo


# 登录
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# 注册
class RegistrationForm(forms.ModelForm):
    # 这里重新定义则不需要下面再声明
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords do not match.')
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme', 'photo')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
