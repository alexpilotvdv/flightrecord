from django.shortcuts import render
from django.http import HttpResponse
from users.models import user,flightday

# Create your views here.
def users(request):
    days=flightday.objects.all()
    return render(request,'index.html',{'flightdays':days})
