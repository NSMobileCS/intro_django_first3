from django.shortcuts import HttpResponse, redirect, render

# Create your views here.
def index_all(request):
    response = 'placeholder for index'
    return HttpResponse(response)    

def index(request):
    response = 'placeholder for blogs'
    return HttpResponse(response)

def new(request):
    response = 'placeholder for blogs\' add blog form'
    return HttpResponse(response)    

def create(request):
    return redirect('/blogs')

def show(request, blog_id):
    response = "<http><head><title>"
    response += blog_id
    response += "</title></head><body>"
    response += "this will have more info about given blog </body></html>"
    return HttpResponse(response)

def edit(request, blog_id):
    response = "this will have more info about given blog in editable form"
    return HttpResponse(response)


def destroy(request, blog_id):
    response = "this will remove given blog"
    return redirect("/blogs")
