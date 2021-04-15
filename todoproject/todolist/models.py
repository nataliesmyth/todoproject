from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# You will start designing your Task data schema by defining the data models for your todolist app. A model is a Python class that subclasses django.db.models.Model in which each attribute represents a database field. Django will create a table for each model defined in the models.py file. By default SQLite database used to store data.

# title: This is the field for the task title. This field is CharField , which translates into a VARCHAR column in the SQL database.
# completed: This field indicates, is task is completed or not. By default, we set False here.
# created: This datetime indicates when the task was created. Since you are using auto_now_add here, the date will be saved automatically when creating an object.
# Here we don’t make primary key, Django model creates automatically for you. you can access it with pk or id.