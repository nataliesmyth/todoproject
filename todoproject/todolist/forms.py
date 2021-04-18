# Form: allows you to build standard forms
# ModelForm: Allows you to build forms tied to model instances

from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        # include all fields in form
        model = Taskfields= "__all__"
        # include particular  fields of model in form
        # fields=('title,completed')