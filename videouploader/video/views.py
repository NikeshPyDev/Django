# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
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

    template_name = 'user/user_list.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        users = User.objects.all()
        print "==ssssssssss",users
        context = {
            'user_list' : users,
        }
        return render(request, self.template_name, context)

class UserCreate(UserPassesTestMixin, SuccessMessageMixin, CreateView):

    template_name = 'user/user_create.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('video:user-list')

    def test_func(self):
        return True

    def get(self, request, *args, **kwargs):
        print "=dddddddddddddddddddddddddd"
        # f = self.form_class()
        # import pdb
        # pdb.set_trace()
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        print "==========post=======",

        form = self.form_class(request.POST)
        user = User.objects.create_user(username=request.POST['username'])
        import pdb
        pdb.set_trace()
        print "==user==", user
        UserProfile.objects.create(user_id= user.id, gender=request.POST['gender'])
        # form.save()
        return HttpResponseRedirect(str(self.success_url))