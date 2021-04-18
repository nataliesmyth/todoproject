from django.shortcuts import render, HttpResponse
from .forms import TaskForm

# Create your views here.


def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    return render(request, "index.html", {"task_form": form})

# We built a form instance with task_form = TaskForm() & pass our form in our template index.html with the context {"task_form":form}
# In our template, we can access this variable with task_form key