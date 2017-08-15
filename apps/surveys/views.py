from django.shortcuts import HttpResponse, redirect, render

# Create your views here.

def index(request):
    return HttpResponse('placeholder for surveys')

def new(request):
    return HttpResponse('placeholder for new survey')

