from django.shortcuts import HttpResponse, redirect, render


# Create your views here.
def demo(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "demo/index.html", context)
