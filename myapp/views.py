from django import http
from django.shortcuts import render,HttpResponse,render
from datetime import datetime
from myapp.models import Contact,detail
# Create your views here.
def index(request):
    event=detail.objects.all()
    return render(request,"index.html", {"event_event":event})

def about(request):
    return render(request,"about.html", )

def contact(request):
     if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        contact=Contact(name=name,email=email,phone=phone,address=address,date=datetime.today())
        contact.save()
      
     return  render(request,"contact.html")
