from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META["REMOTE_ADDR"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
            <br>Path: {path}
            <br>Address: {address}
            <br>Scheme: {scheme}
            <br>Method: {method}
            <br>User agent: {user_agent}
            <br>Path info: {path_info}
            <br>Response header: {response.headers}
           
            """
            

    #response = HttpResponse("This works!")
    #return response
    return HttpResponse(msg, content_type = 'text/html', charset='utf-8')

def homepage(request):
    return HttpResponse('Welcome to Little Lecmon restaurant') 

def say_hello(request):
    return HttpResponse("Hello World")  

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style = "color: #F4CE14;"> This is Little Lemon Again!</h1"""
    return HttpResponse(text)

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def myview(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 
        context={ } #dict containing data to be sent to the client  
    return render(request, 'mytemplate.html', context) 



#Sub-class of the View class
#     from django.views import View 
# class MyView(View): 
#     def get(self, request): 
#         # logic to process GET request
#         return HttpResponse('response to GET request') 
 
#     def post(self, request): 
#         # <logic to process POST request> 
#         return HttpResponse('response to POST request') 
#-----
# Generic views:
# TemplateView, CreateView, ListView, DetailView, UpdateView 