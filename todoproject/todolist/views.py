from django.shortcuts import render, HttpResponse
from .forms import TaskForm

# Create your views here.
def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    return render(request, "index.html", {"task_form": form})