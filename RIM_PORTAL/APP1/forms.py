from django import forms
from .models import Issue
from django.contrib.auth.models import User

from django.contrib.auth.models import User , auth



class PostForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['show','sys_creation_date','user']



