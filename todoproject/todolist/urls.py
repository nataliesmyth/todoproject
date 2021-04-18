from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    # takes the pk arguments and maps it to the update_task view
    path('update/<int:pok>/', views.update_task, name="update task"),
]