from django.shortcuts import render
from kbjcrm.control import Control

# Create your views here.

def rcp(request):
    if request.method == 'POST':
        year = request.POST.get('Year')
        lv_list = Control.select(year)
        return render(request, 'views/rcp_view.html', {'obj': lv_list, 'rcplist': lv_list})
    return render(request, 'views/rcp_view.html', {'obj': '', 'rcplist': Control.select_all(Control)})