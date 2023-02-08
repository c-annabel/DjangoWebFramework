from django.http import HttpResponse, HttpResponseNotFound

def handler400(request, exception):
    return HttpResponse("400: Bad Request! ")

def handler403(request, exception):
    return HttpResponse("403: Forbidden")

def handler404(request, exception):
    return HttpResponse("404: Page not Found! <br><br> <button onclick="" href=''; ""> Go to Homepage </button>")

def handler500(request, exception):
    return HttpResponse("500: Server Eroor! ")

def homepage(request):
    return HttpResponseNotFound(" Little Lemon !")