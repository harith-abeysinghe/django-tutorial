from django.shortcuts import render
from django.http import HttpResponse

# django uses MVT (Model-View-Template architecture).


# The view is responsible for processing the request and returning the response. 
# The view is a Python function that takes a web request and returns a web response.
# The view function receives web requests and returns web responses
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")