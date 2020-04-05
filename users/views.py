from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from users.models import user,flightday

# Create your views here.
def users(request):
    days=flightday.objects.all()
    return render(request,'index.html',{'flightdays':days})
def day_detail(request,day_id):
    day=get_object_or_404(flightday,id=day_id)
    return render(request,'detail_day.html',{'detail_day':day})
