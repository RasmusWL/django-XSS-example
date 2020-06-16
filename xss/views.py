from django.http import HttpRequest, HttpResponse

def hello(request: HttpRequest, name: str):
    return HttpResponse("Hello {}".format(name))
