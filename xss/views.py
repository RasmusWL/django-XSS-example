from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

def hello(request: HttpRequest, name: str):
    return HttpResponse("Hello {}".format(name))

def hello404(request: HttpRequest, name: str):
    return HttpResponseNotFound("Hello {}".format(name))
