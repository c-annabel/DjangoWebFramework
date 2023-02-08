from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect
# from .models import Product
from django.urls import reverse
from datetime import datetime

# Create your views here.
def detail(request, id):
    try:
        p=Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse("Product Found")

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
    content = "<html><body><h1>Welcome</h1></body></html>"
    return HttpResponse(content) 
    # return HttpResponse('Welcome to Little Lecmon restaurant') 

def login(request):
    return render(request, "form.html")
    # return HttpResponse('Log in') 

# def myview(request):
#     return HttpResponsePermanentRedirect(reverse('myapp:login'))

def index(request):
    return HttpResponse('index') 

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
        # form = Myform(request.POST)
        # if form.is_valid():
        #     pass
        # else:
        #     return HttpResponse("Form submitted with invalid data")
        #perform insert or update operation on the model 
        context={ } #dict containing data to be sent to the client  
    return render(request, 'mytemplate.html', context) 

    # if condition == True:
    #     return HttpResponse('<h1>Page not found</h1>'), status_code = '404')
    # else:
    #     return HttpResponse('<h1>Page was found</h1>')

    #The view function obtains the body parameters in the client’s request 
    #with its _request.POST_____________ attribute.
    #When an HTML form submits data with the POST method, it is added to the body of the HTTP request. Inside the view function, the request.POST attribute fetches the form data for further processing.


def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from combination of wheat, water or eggs.',
        'falafel': 'Falafel are deep fried patties or balls made from ...',
        'cheesecake': 'Cheesecake is a type of dessert made with cream, soft cheese on top of cookie, pastry crust or graham cracker and fruit sauce topping.'
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish.title()} </h2>"+  description)

def display_menu_item(request):
    pass

# def qryview(request): 
#     name = request.GET['name'] 
#     id = request.GET['id'] 
#     return HttpResponse("Name:{} UserID:{}".format(name, id)) 

#Sub-class of the View class (class-instance views)
#     from django.views import View 
#     class MyView(View): 
#       def get(self, request): 
#             # logic to process GET request
#              return HttpResponse('response to GET request') 
 
#       def post(self, request): 
#              # <logic to process POST request> 
#              return HttpResponse('response to POST request') 
#-----
# Generic views:
# TemplateView, CreateView, ListView, DetailView, UpdateView 


# What are the types of parameters that a view receives in a client request?

# Path parameters
# If the client URL endpoint contains one or more parameters separated by the / symbol, the path converter in path() function’s URL pattern string parses the parameters in appropriate variables. Then, it passes them to the view function.
# Body Parameters
# The data items sent by the client with POST method are the body parameters of the request. The request.POST attribute contains this data.
# Query Parameters
# The URL may have a query string appended to the endpoint. The parameters are available to the view in request.GET attribute.