from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def users(request):
    return render(request,'index.html',{'insert_me':"jjjjjjjjjjjjjj"})
