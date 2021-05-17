from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .models import TodoListItem
from django.views import generic
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from .models import TodoListItem
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

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
        return TodoListItem.objects.all().order_by('-time')

class SearchView(generic.ListView):
    model = TodoListItem
    template_name = 'todoApp/todoList.html'
    context_object_name = 'filter_items'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return TodoListItem.objects.filter(content__icontains = query)

class AboutView(generic.TemplateView):
    template_name = 'todoApp/about.html'

"""class ContactView(generic.FormView):
    template_name = "todoApp/contact.html"
    form_class = forms.ContactForm
    def form_valid(self, form):
        subject = 'Contact'
        body = {
            'first_name':form.cleaned_data['first_name'],
            'last_name':form.cleaned_data['last_name'],
            'email':form.cleaned_data['email'],
            'message':form.cleaned_data['message'],
        }
        message = '\n'.join(body.values())
        send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['vinitrathodmeera@gmail.com'],
        fail_silently=False)
        return super().form_valid(form)"""

def contactView(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact'
            body = {
                'first_name':form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'email':form.cleaned_data['email'],
                'message':form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject,message,body['email'],['vinitrathod123@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('index')

    form = forms.ContactForm()
    return render(request,'todoApp/contact_us.html',{'form':form})

#@login_required(login_url='login')
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
    y = TodoListItem.objects.get(id = i)
    last_item = TodoListItem(content = y.content,done = True)
    last_item.save()
    y.delete()
    return HttpResponseRedirect('/')

def register(request):
    form = forms.CreateUserForm()
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            users = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'users')
            users.groups.add(group)

            messages.success(request,'Account Created for '+username)

            return redirect('login')
    return render(request,'todoApp/register.html',{'form':form})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = authenticate(request,username=username,password=password)

        if users is None : 
            login(request,users)
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request,'todoApp/login.html',{})