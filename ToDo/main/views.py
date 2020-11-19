
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt #For csrf exemption
from django.utils import timezone#To give the timezone and time of creation to database
from .models import toDo
 # Create your views here.
def home(request):
    toDo_list=toDo.objects.all().order_by('date_entered')
    #Get all data in dataBase and put into the html page
    #.order_by() It oders by date what enter first
    context={
        'toDo':toDo_list
    }
    return render(request,"index.html",context)
@csrf_exempt
def add_todo(request):
        content=request.POST['content']
        date_time=timezone.now()
        toDo.objects.create(date_entered=date_time,text=content)#To give content to database
        length_of_models=toDo.objects.all().count()
        print(length_of_models,content,date_time)
        return redirect('/')
@csrf_exempt
def delete_todo(request,todo_id):
    
        toDo.objects.get(id=todo_id).delete()
        return redirect('/') 
