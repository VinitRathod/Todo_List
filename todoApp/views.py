from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import TodoListItem
from django.views import generic

# Create your views here.
"""def index(request):
    all_todo_items = TodoListItem.objects.all()
    context = {
        'all_items':all_todo_items
    }
    return render(request,'todoApp/todoList.html',context)
    #return HttpResponse('Hello from TodoApp')"""

class IndexView(generic.ListView):
    template_name = 'todoApp/todoList.html'
    #context_object_name is by default object_list
    #for changing it do the below code
    context_object_name = 'all_items'
    
    def get_queryset(self):
        return TodoListItem.objects.all()

def addtoview(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodoView(request,i):
    y = TodoListItem.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/')

def deleteAllContents(request):
    y = TodoListItem.objects.all()
    y.delete()
    return HttpResponseRedirect('/')

def doneItems(request,i):
    y = TodoListItem.objects.all().filter(id = i).order_by('i')[::-1]
    y.save()
    return HttpResponseRedirect('/')


