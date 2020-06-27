from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'portfolio/home2.html',{'projects':projects})

def message(request):
    print("jaihind")
    return render(request,'portfolio/message.html')
def check(request):
    name = request.POST['fname'] # u_name is the name of the input tag
    lname = request.POST['lname']
    #return render(request,'test.html',{'k':name})

def mailfunc(request):
    name= request.POST.get('name')
    ph = request.POST.get('ph')
    message = request.POST.get('message')
    know = request.POST.get('know')
    email = request.POST.get('email')
    fmessage=' from ' + name +'  email is  '+email+ '  ph is  ' + ph + '  message  is  ' + message
    lname='walia'
    send_mail(
    'My website click',
    fmessage ,
    'himanshuwalia099@gmail.com',
    ['himanshuwalia099@gmail.com'],
    fail_silently=False,)
    return render(request, 'portfolio/index.html')
def skillbar(request):
    return render(request, 'portfolio/skillbar.html')
def skillbarTools(request):
    return render(request, 'portfolio/skillbarTools.html')
def skillbarFrameworks(request):
    return render(request, 'portfolio/skillbarFrameworks.html')






