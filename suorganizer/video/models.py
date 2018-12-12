from django.db import models


class Video(models.Model):

    name = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
