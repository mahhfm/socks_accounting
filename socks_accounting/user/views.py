from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from random import randint
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
import jdatetime
from datetime import date
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    # DeleteView,
)
from django.views.generic.edit import DeleteView
from rest_framework import routers, serializers, viewsets
from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic import TemplateView
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from  paramiko import SSHClient


def home(request):
    return render(request, 'user/base.html')



class ProfileListView(ListView):
    template_name = 'user/show_data.html'
    context_object_name = 'profiles' 
    model = Profile

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user/new.html'
    success_url = '/user/profiles/'
    def form_valid(self, form):
        data = form.cleaned_data
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname ='mehditaleblo.ir', port = '33033', password = 'mmt123@' , username = 'root', allow_agent=True)
        stdin, stdout, stderr = client.exec_command('useradd ' + data['username'] +  ' --shell /bin/false && echo -e "' + data['password'] +'\n ' + data['password'] + '\n" +  | passwd ' + data['username']  )
        new_user = User.objects.create(
                username=data.pop('username'),
                first_name=data.pop('first_name'),
                last_name=data.pop('last_name'),
                email=data.pop('email'),
                password=make_password(data.pop('password')),
            )
        data.pop('re_password'),
        new_profile = form.save(commit=False)
        new_profile.user = new_user
        return super().form_valid(form)


# class ModelCreateView(CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'edu/new.html'
#     success_url = '/student/'


# class ShowDetail(DetailView):
#     template_name = 'edu/show_data.html'


# class ModelUpdateView(UpdateView):

#     fields = "__all__"
#     template_name = "edu/update.html"
#     path_name = ''


# class DeleteModelView(DeleteView):
#     model = Course
#     template_name = 'edu/delete_object.html'
#     success_url = ''
#     path_name = ''


class LoginViewClass(LoginView):
    template_name="user/login.html"
