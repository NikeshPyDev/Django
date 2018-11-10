# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View
from django.contrib import auth

# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('video:user_details')

class UserList(UserPassesTestMixin, View):

    template_name = 'registration/user_list.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        users = User.objects.all()
        print "==ssssssssss",users
        context = {
            'user_list' : users,
        }
        return render(request, self.template_name, context)