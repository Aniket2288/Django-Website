import email
from urllib import request
from django.shortcuts import render , HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(requests):
    context = {
        "variable" : "This is sent"
    }
    return render(requests,'index.html', context)
    # return HttpResponse('This is the Home Page')

def about(requests):
    return render(requests,'about.html')
    # return HttpResponse('This is the About Page')

def services(requests):
    return render(requests,'services.html')
    # return HttpResponse('This is the services Page')

def contact(requests):
    if requests.method == "POST":
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        phone = requests.POST.get('phone')
        contact = Contact(name=name, email=email, phone=phone)
        contact.save()
        messages.success(requests, "Your Information is Updated")
    return render(requests,'contact.html')
    # return HttpResponse('This is the contact Page')

    