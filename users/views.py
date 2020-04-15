from django.shortcuts import render, get_object_or_404, redirect
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
from .forms import UserCreateForm, FillProfile

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
            if not user.objects.filter(user_reg=request.user).exists():
                #если нет записи в профиле
                #создаем новую
                profil=user()
                profil.user_reg=request.user
                profil.save()

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

class ProfileUpdate(View):
    def get(self,request):
        if request.user.is_authenticated:
            if not user.objects.filter(user_reg=request.user).exists():
                #если нет записи в профиле
                #создаем новую
                profil=user()
                profil.user_reg=request.user
                profil.save()
            userobj=user.objects.get(user_reg=request.user)
            profilform=FillProfile(instance=userobj)
            return render(request,'users/updateprofil.html',context={'form':profilform})
    def post(self,request):
        if request.user.is_authenticated:
            userobj=user.objects.get(user_reg=request.user)
            profilform=FillProfile(request.POST,request.FILES,instance=userobj)
            if profilform.is_valid():
                new_userobj=profilform.save(userparam=request.user)
                return redirect('main')
            return render(request,'users/updateprofil.html',context={'form':profilform})



class ProfileFormView(FormView):
    form_class = FillProfile
    success_url="/"
    template_name="users/profile.html"
    #чтобы определить пользователя
    def post(self, request, *args, **kwargs):
        self.userid=request.user
        return super(ProfileFormView,self).post(self, request, *args, **kwargs)


    def form_valid(self,form):
        #print(self.curuser)
        form.save(userparam=self.userid)
        return super(ProfileFormView,self).form_valid(form)

    def form_invalid(self,form):
        return super(ProfileFormView,self).form_invalid(form)
