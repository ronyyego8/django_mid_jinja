from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about.html")


def contact_us(request):
    return render(request,"contact.html")

def gallery(request):
    return render (request,'gallery.html')
