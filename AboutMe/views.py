from django.shortcuts import render,get_object_or_404
from .models import AboutMe

# Create your views here.
def aboutMe(request):
    aboutmeobjs=AboutMe.objects.all()
    #return render(request,'aboutme/aboutme2.html',{'aboutmeobjs':aboutmeobjs})
    return render(request, 'aboutme/aboutmehome.html', {'projects': aboutmeobjs})

def detail(request,aboutme_id):
    obj=get_object_or_404(AboutMe,pk=aboutme_id)
    return render(request,'aboutme/detail.html',{'obj':obj})
