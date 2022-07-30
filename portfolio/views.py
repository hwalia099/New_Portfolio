from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'portfolio/hometest.html',{'projects':projects})

def message(request):
    print("jaihind")
    return render(request,'portfolio/message.html')
def check(request):
    name = request.POST['name'] # u_name is the name of the input tag
    #lname = request.POST['name']
    #return render(request,'test.html',{'k':name})
def resume(request):
    return printPdf('/home/HimanshuWalia/personal-portfolio-django3/static/portfolio/esume.pdf')
def printPdf(path):
    with open(path, "rb") as f:
        data = f.read()
    return HttpResponse(data, content_type='application/pdf')
def mailfunc(request):
    name= request.POST.get('name')
    sub = request.POST.get('subject')
    message = request.POST.get('message')
    email = request.POST.get('email')
    fmessage=' from ' + name +'  email is  '+ email +   '  message  is  ' + message
    send_mail(
    'My website click -- '+ sub,
    fmessage ,
    'himanshuwalia099@gmail.com',
    ['himanshuwalia099@gmail.com'],
    fail_silently=False,)
    return render(request, 'portfolio/message.html')
def skillbar(request):
    return render(request, 'portfolio/skillbar.html')
def skillbarTools(request):
    return render(request, 'portfolio/skillbarTools.html')
def skillbarFrameworks(request):
    return render(request, 'portfolio/skillbarFrameworks.html')






