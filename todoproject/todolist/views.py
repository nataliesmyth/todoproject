from django.shortcuts import redirect, render, HttpResponse
from .forms import TaskForm
from .models import Task

# Create your views here.


def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()

    if request.method == "POST":
        # Get the posted form
        # the form send us back to our view when we hit submit, so we handle it below
        # Instantiate the form
        form = TaskForm(request.POST)
        # if form isn't valid, template with validation errors is rendered
        if form.is_valid():
            # if the form is valid, a new task will be stored in the database 
            form.save()
            # Then we redirect to the index page (redirect() method is Django's shortcut to redirect any URL)
            return redirect("index")

    tasks= Task.objects.all()
    return render(request, "index.html", {"task_form": form, "tasks": tasks})

# Update Task view
# this view takes the pk argument to retrieve a particular task within the given id/pk
def update_task(request, pk):
    task = Task.objects.get(id=pk)

    # We get a particular task in our form by passing task instance to our form to update it
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "update_task.html", {"task_edit_form": form})

# We built a form instance with task_form = TaskForm() & pass our form in our template index.html with the context {"task_form":form}
# In our template, we can access this variable with task_form key

# 2 kinds of HTTP requests
    # GET and POST
    # In djnago, the req object passed as parameter to your view has an attribute called "method" where the type of the request is set, and all data passed via POST can be accessed via the request.POST dictionary