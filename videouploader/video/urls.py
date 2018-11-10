from django.conf.urls import url
from .views *

urlpatterns = [
    url(r'^users', UserList.as_view(), name='user-list')
]

