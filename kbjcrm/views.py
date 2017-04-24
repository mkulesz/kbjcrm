from django.shortcuts import render
from kbjcrm.models import Kontrakt
from kbjcrm.models import models

# Create your views here.
from django.http import HttpResponse

def views(request):
    return render(request, 'views/first_view.html', {})

def rcp(request):
    query = Kontrakt.objects.all()
    return  render(request, 'views/rcp_view.html', {'obj': Kontrakt.objects.all()})