from django.shortcuts import render
from kbjcrm.control import Control

# Create your views here.
from django.http import HttpResponse

def views(request):
    return render(request, 'views/first_view.html', {})

def rcp(request):
#    year = request.POST['Year']
    lv_list = Control.Select(2017)
    return render(request, 'views/rcp_view.html', {'obj': lv_list})