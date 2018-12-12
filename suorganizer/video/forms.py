from django import forms
from .models import Video


class UploadVideoForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    upload = forms.FileField()
    class Meta:
        model = Video
        fields = ['name', 'upload']

