from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def views(request):
    return render(request, 'views/first_view.html', {})

def rcp(request):
    return  render(request, 'views/rcp_view.html', {})