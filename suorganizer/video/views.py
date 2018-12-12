# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from PIL import Image
from io import BytesIO
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import UploadVideoForm
from .models import Video
from django.views.generic.edit import FormView


class VideoManagerView(FormView):

    form_class = UploadVideoForm
    template_name = 'video_upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/video')


def video_list(request):
    data = {
        'videos': Video.objects.all()
    }
    return render(request, 'video_list.html', data)


def download_video(request, *args, **kwargs):
    path = kwargs.get('path', False)
    print("path=", path, os.path.exists(path))
    if path and os.path.exists(path):
        with open(path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='video/mp4')
            return response



