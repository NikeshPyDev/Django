from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'max': '30', 'class': 'span6', 'autofocus': 'autofocus'}), required=True)
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'max': 30}), required=True)
    gender = forms.ChoiceField(label='Gender',choices=[(0, 'Male'), (1, 'Female')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}))

    class Meta:
        model = UserProfile
        fields = ['first_name', 'username', 'gender']