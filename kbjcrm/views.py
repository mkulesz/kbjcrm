from django.shortcuts import render
from kbjcrm.control import Control

# Create your views here.

def rcp(request):
    if request.method == 'POST':
        year = request.POST.get('Year')
        lv_list = Control.Select(year)
        return render(request, 'views/rcp_view.html', {'obj': lv_list})
    return render(request, 'views/rcp_view.html', {'obj': ''})