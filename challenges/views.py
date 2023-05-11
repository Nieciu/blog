from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("Run 3km a day")


def february(request):
    return HttpResponse("Don't eat as much")


def march(request):
    return HttpResponse("Practice guitar an hour per day")
