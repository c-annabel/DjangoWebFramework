"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views

handler400 = "demoproject.views.handler400" # HttpResponseBadRequest
handler403 = "demoproject.views.handler403" # HttpResponseForbidden
handler404 = "demoproject.views.handler404" # HttpResponseNotFount
# handler500 = "demoproject.views.handler500" # HttpResponseServerError

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name= 'homepage'),
    path('say_hello/', views.say_hello),
    path('display_date/', views.display_date),
    path('menu/', views.menu),
    path('', include('myapp.urls', namespace='myapp'))
    #path('main/', include('myapp.urls')),
    # path('dishes/<str:dish>', views.menuitems, name='dish'),
    #angular brackets
]
