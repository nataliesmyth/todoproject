from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form

    title = forms.Charfield(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter a task...",
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-check-input"}),
    )


# To create a form from a model, you just need to indicate which model to use to build the form in the Meta class of the form.
# Django will them introspect the model and build the form dynamically