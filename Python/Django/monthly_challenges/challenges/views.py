from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("eat no meat for 1 month")

def february(request):
    return HttpResponse("Walk 20 min everyday!")
