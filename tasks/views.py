from django.shortcuts import render , redirect
from .models import mytask

# Create your views here.
def home(request):
    tasks = mytask.objects.all()
    return render(request,'main.html',{'tasks':tasks})

def addtask(request):
    taskdescription = request.POST['task']
    loc = request.POST['location']
    taskdate = request.POST['date']
    tasktime = request.POST['time']
    mytask(task=taskdescription,location=loc,date=taskdate,time=tasktime).save()
    return redirect('/')