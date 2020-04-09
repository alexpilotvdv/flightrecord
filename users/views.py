from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from users.models import user,flightday
#для регистрации пользователя
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View

# Create your views here.
def users(request):
    days=flightday.objects.all()
    return render(request,'index.html',{'flightdays':days})
def day_detail(request,day_id):
    day=get_object_or_404(flightday,id=day_id)
    return render(request,'detail_day.html',{'detail_day':day})

def main_page(request):
    return render(request,'index.html')
#регистрация нового пользователя
class RegisterFormView(FormView):
    form_class=UserCreationForm
    success_url="/login/"
    template_name="users/register.html"
    def form_valid(self,form):
        form.save()
        return super(RegisterFormView,self).form_valid(form)

# аутентификация
        

#выход пользователя
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")
