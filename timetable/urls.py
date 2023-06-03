from django.urls import path
from . import views

app_name = 'timetable'

urlpatterns = [
    path('index', views.index, name='index'),
    path('create', views.creation, name='create'),
    path('save', views.save_seed, name='save'),
]