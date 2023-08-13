from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Task
from django.http import JsonResponse
# Create your views here.

def Home(request):
    tasks = Task.objects.all().order_by('-updated_at')
    is_completed = True
    comTasks = Task.objects.filter(is_completed=is_completed).order_by('-updated_at')
    #adding task
    if request.method == 'POST' or request.method == 'post':
        taskAdd = request.POST.get('add', '')
        task = Task(task=taskAdd)
        task.save()
        
        return redirect('todo')
    context = {
        'tasks':tasks,
        'comTasks':comTasks
    }
    return render(request, 'home_todo.html',context)


def mard_as_done(request,pk):
    task = get_object_or_404(Task,id=pk)     
    task.is_completed = True
    task.save()
    return redirect('todo')

def delete_task(request,pk):
    task = get_object_or_404(Task,id=pk)
    task.delete()
    return redirect('todo')

def undo_task(request,pk):
    task = get_object_or_404(Task,id=pk)
    task.is_completed = False
    task.save()
    return redirect('todo')




def get_task_content(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task_content = task.task
    data = {'task_content': task_content}
    return JsonResponse(data)



def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        updated_task_content = request.POST.get('updateTask','')
        task.task = updated_task_content
        task.save()
        return redirect('todo')
    context ={
        'task':task,
        'task_id':task_id
    }
    return render(request,'home_todo.html',context)


    
