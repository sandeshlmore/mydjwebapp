from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def homePage(request):
    return HttpResponse("Hello world")

class homepageView(TemplateView):
    template_name = 'home.html'

class aboutPageView(TemplateView):
    template_name = 'about.html'

