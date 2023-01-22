from django.urls import path
from . import views   #dot (.) here indicates the same working directory as the file.

urlpatterns = [
    path('', views.home), 
]