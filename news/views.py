from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from django.contrib.auth import logout

# Create your views here.
class NewsView(ListView):
    model = News
    template_name = 'news.html' #This is a class based view

class PostDetail(DetailView):
    model = News
    template_name = 'detail.html' #This is a class based view
    context_object_name = 'post' #This is a class based view

class Create_post(CreateView):
    model = News
    template_name = 'create.html'
    fields = ['title', 'text', 'author']

class Update_post(UpdateView):
    model = News
    template_name = 'update.html'
    fields = ['title', 'text']

class Delete_post(DeleteView):
    model = News
    template_name = 'delete.html'
    success_url = '/'

def Log_out(request):
    success_url = '/'
    logout(request)
    return redirect(success_url)