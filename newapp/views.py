from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html' #This is a class based view

class AboutView(TemplateView):
    template_name = 'about.html' #This is a class based view
