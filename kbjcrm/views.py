from django.shortcuts import render
from kbjcrm.control import Control

# Create your views here.

def rcp(request):
    if request.method == 'POST':
        if 'List' in request.POST:
            year = request.POST.get('Year')
            return render(request, 'views/rcp_view.html', {'obj': Control.select(year), 'rcplist': Control.select(year)})
        if 'Generator' in request.POST:
            number = request.POST.get('Generator_num')
            return render(request, 'views/rcp_view.html', {'obj': '', 'rcplist': Control.select_all(Control), 'gen_number': number})
    return render(request, 'views/rcp_view.html', {'obj': '', 'rcplist': Control.select_all(Control)})