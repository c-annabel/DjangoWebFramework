from django.urls import path, re_path, reverse
from . import views   #dot (.) here indicates the same working directory as the file.

app_name = 'myapp'

urlpatterns = [
    path('', views.homepage),
    path('login/', views.login, name = 'login'),
    path('index/', views.index, name = 'index'),
    # path('home/', views.home, name="home"), 
    path('dishes/<str:dish>', views.menuitems, name='dish'),
    path('menu_item/10', views.display_menu_item),
    #RegEx URL
    re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item),
    #path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    #path('getuser/', views.qryview, name='qryview') 
]