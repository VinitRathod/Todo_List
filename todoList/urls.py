"""todoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from todoApp.views import (addtoview,IndexView,deleteTodoView,
                           deleteAllContents,doneItems,contactView,
                           SearchView,register,sign_in,AboutView)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('todoApp/',include('todoApp.urls')),
    path('',IndexView.as_view(),name = 'index'),
    path('addTodoItem/',addtoview),
    path('deleteTodoItem/<int:i>/',deleteTodoView),
    path('deleteAllItems/',deleteAllContents),
    path('doneitem/<int:i>/',doneItems),
    path('contactus/',contactView,name='contact_us'),
    path('search/',SearchView.as_view()),
    path('register/',register,name="register"),
    path('login/',sign_in,name="login"),
    path('about/',AboutView.as_view(),name='about')
]
