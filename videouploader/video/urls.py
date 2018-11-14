from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^users', UserList.as_view(), name='user-list'),
    url(r'^new_user', UserCreate.as_view(), name='user-create')
]

