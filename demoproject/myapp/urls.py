from django.urls import path
from . import views   #dot (.) here indicates the same working directory as the file.

urlpatterns = [
    path('home/', views.home, name="home"), 
    
    #path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    #path('getuser/', views.qryview, name='qryview') 
]
