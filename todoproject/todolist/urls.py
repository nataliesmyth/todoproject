from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('update/<int:pok>/', views.update_task, name="update task"),
]