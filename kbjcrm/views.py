from django.shortcuts import render
from kbjcrm.control import Control


# Create your views here.

def rcp(request):
    if request.method == 'POST':
        if 'List' in request.POST:
            year = request.POST.get('Year')
            return render(request, 'views/rcp_view.html',
                          {'obj': Control.select(year), 'rcplist': Control.select_all(Control)})
        if 'Generator' in request.POST:
            number = request.POST.get('Generator_num')
            if int(number) > 0:
                idrcp = request.POST.get('RCPList', None)
                Control.generate(number, idrcp)
                return render(request, 'views/rcp_view.html',
                              {'obj': '', 'rcplist': Control.select_all(Control), 'idkonta': number})
    return render(request, 'views/rcp_view.html', {'obj': '', 'rcplist': Control.select_all(Control)})
