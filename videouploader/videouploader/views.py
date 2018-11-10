import logging
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

log_file = logging.getLogger('admin')

class Login(View):
    template_name = 'registration/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'username' in request.POST and 'password' in request.POST:
            user_authenticate = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user_authenticate and user_authenticate.is_superuser:
                log_file.info('User "%s" logged in successfully' % (request.POST.get('username')))
                auth_login(request, user_authenticate)
                return HttpResponseRedirect(request.GET.get('next', '/admin/'))
            elif user_authenticate and not user_authenticate.is_superuser:
                log_file.warning('User "%s" tried to log in to admin to admin panel' % (request.POST.get('username')))
                messages.error(request, "You don't have permission to access.")
            else:
                messages.error(request, 'Invalid username or password!!')
        else:
            messages.error(request, 'Username and password not found!!')
        return render(request, self.template_name)

#     def get(self, request):
#         if request.user.is_authenticated():
#             return render(request, self.template_name)
#         else:
#             return render(request, self.template_name)
#
#     def post(self, request):
#         if 'username' in request.POST and 'password' in request.POST:
#             user_authenticate = authenticate(username=request.POST['username'], password=request.POST['password'],
#                                              backend='django.contrib.auth.backends.ModelBackend')
#             if user_authenticate and user_authenticate.is_superuser:
#                 log_file.info('User "%s" logged in successfully' % (request.POST.get('username')))
#                 auth_login(request, user_authenticate, backend='django.contrib.auth.backends.ModelBackend')
#                 return HttpResponseRedirect(request.GET.get('next', '/admin/'))
#             elif user_authenticate and not user_authenticate.is_superuser:
#                 log_file.warning('User "%s" tried to log in to admin panel' % (request.POST.get('username')))
#                 messages.error(request, "You don't have permission to access this area. Please contact administrator.")
#             else:
#                 messages.error(request, 'Invalid username or password!!')
#         else:
#             messages.error(request, 'username and password not found!!')
#         return render(request, self.template_name)
#
class Dashboard(UserPassesTestMixin, View):

    template_name = 'registration/dashboard.html'

    def test_func(self):
        return True

    def get(self, request):
        return render(request, self.template_name)

# class UserList(UserPassesTestMixin, View):
#
#     template_name = 'registration/user_list.html'
#
#     def test_func(self):
#         return self.request.user.is_superuser
#
#     def get(self, request):
#         users = User.objects.all()
#         print "==ssssssssss",users
#         context = {
#             'user_list' : users,
#         }
#         return render(request, self.template_name, context)

