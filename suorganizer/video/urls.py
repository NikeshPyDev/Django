from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='track_list'),
    path('upload', views.VideoManagerView.as_view(), name='upload_video'),
    path('download/(?P<path>[\w\-]+)/$', views.download_video, name='download_video')
]