from django.forms import ModelForm
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user

class UserCreateForm(UserCreationForm):
    email=forms.EmailField(required=True)
    prov=forms.CharField(max_length="10")
    #попробовал добавить проверочное поле в форму
    prov.label="Проверочный код"

    class Meta:
        model=User
        fields=("username","email","password1","password2","prov")

    def save(self,commit=True):
        user=super(UserCreateForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    #проверка поля
    def clean(self):
        cleaned_data=super(UserCreateForm,self).clean()
        prov_val=cleaned_data.get("prov")
        if '120' not in prov_val:
            msg="Не правильный проверочный код!"
            self._errors["prov"]=self.error_class([msg])
            #del cleaned_data["prov"]
        return cleaned_data

class FillProfile(ModelForm):
    class Meta:
        model = user
        fields = ['foto','nik','firstname','lastname','pfone','dborn','email']
