from django.shortcuts import render,redirect,HttpResponse
from django.urls import path
import shutil
from . import views
from .models import event
# Create your views here.

def index(request):
    allevent=event.objects.all()
    evt={
        "event_all":allevent
    }

    return render(request,'index.html',evt)

def addformdata(request):
    print("golu")
    evt_name=request.POST["evt_name"]
    evt_location=request.POST["evt_location"]
    evt_date=request.POST["evt_date"]
    evt_time=request.POST["evt_time"]
    evt_image=request.POST["evt_image"]
    
    event_obj=event(ename=evt_name,elocation=evt_location,edate=evt_date,etime=evt_time,image=evt_image)
    event_obj.save()
   
    return redirect("/")

def liked(request):
    event1=event.objects.filter(elike='t')
    liked={
        "liked":event1
    }

    return render(request,'index.html',liked)

def statuslike(request):
    if request.method == 'POST':
        if 'eno' in request.POST: 
             eno = request.POST['eno']
             obj=event.object.get(pk=eno)
             obj.elike='t'
             obj.save()
             return HttpResponse('success')
    return HttpResponse('failed')         