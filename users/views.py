from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from users.models import user,flightday
from django.views.generic import TemplateView
#для регистрации пользователя
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.views.generic.base import View
from .forms import UserCreateForm

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
    form_class=UserCreateForm
    success_url="/login/"
    template_name="users/register.html"
    def form_valid(self,form):
        #вариант проверки проверочного поля
        #print(form.cleaned_data['prov'])
    #    if (form.cleaned_data['prov'] == '120'):
            form.save()
            return super(RegisterFormView,self).form_valid(form)
        #else:
            #return super(RegisterFormView,self).form_invalid(form)

    def form_invalid(self,form):
        return super(RegisterFormView,self).form_invalid(form)


class MainView(TemplateView):
    template_name="index.html"
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,self.template_name,{})
        else:
            return render(request,self.template_name,{})


# аутентификация
class LoginFormView(FormView):
    form_class=AuthenticationForm
    template_name="users/login.html"
    success_url="/"
    def form_valid(self,form):
        self.user=form.get_user()
        login(self.request,self.user)
        return super(LoginFormView,self).form_valid(form)


#выход пользователя
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")
