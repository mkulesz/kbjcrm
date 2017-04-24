from django.shortcuts import render
from kbjcrm.control import Control
from django.forms import Form

# Create your views here.
from django.http import HttpResponse

def views(request):
    return render(request, 'views/first_view.html', {})

def rcp(request):
    if request.method == 'POST':
        year = request.POST.get('Year')
        lv_list = Control.Select(year)
        return render(request, 'views/rcp_view.html', {'obj': lv_list})
    return render(request, 'views/rcp_view.html', {'obj': ''})