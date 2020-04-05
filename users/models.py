from django.db import models
from datetime import datetime

# модель членов клуба.
class user(models.Model):
    foto = models.ImageField('Фото',upload_to='users/foto',default='',blank=True)
    nik = models.CharField(max_length=15,verbose_name='Ник')
    firstname = models.CharField(max_length=15,verbose_name='Имя')
    lastname = models.CharField(max_length=15,verbose_name='Фамилия')
    pfone = models.CharField(max_length=12,blank=True,verbose_name='Телефон')
    dborn = models.DateField(auto_now=False,auto_now_add=False,blank=True,verbose_name='Дата рождения')
    email = models.EmailField(max_length=50,blank=True,verbose_name='Email')
    rate = models.IntegerField(default=0,verbose_name='Рейтинг')
    class Meta:
        verbose_name='Член клуба'
        verbose_name_plural='Члены клуба'
        ordering=['lastname']
    def __str__(self):
        return self.lastname
#модель летных дней
class flightday(models.Model):
#    chlen = models.ForeignKey(user,on_delete=models.SET_NULL)
    data = models.DateField(auto_now=False,unique=True,auto_now_add=False,blank=True,verbose_name='Дата полетов')
    timestart = models.TimeField(auto_now=False,auto_now_add=False,blank=True,verbose_name='Время начала полетов')
    timefinish = models.TimeField(auto_now=False,auto_now_add=False,blank=True,verbose_name='Время окончания полетов')
    nalet = models.TimeField(auto_now=False,auto_now_add=False,blank=True,verbose_name='Максимальный налет')
    info = models.TextField(blank=True,verbose_name='Дополнительная информация')
    regopen = models.BooleanField(default=False,verbose_name='Регистрация открыта')
    class Meta:
        verbose_name='День полетов'
        verbose_name_plural='Дни полетов'
        ordering=['data']
    def __str__(self):
        datetimeObj=self.data
        dateStr=datetimeObj.strftime('%d-%b-%Y')
        return dateStr
# непосредственно записи на полеты
class zapisi(models.Model):
    chlen = models.ForeignKey(user,on_delete=models.PROTECT)
    data_poleta = models.ForeignKey(flightday,on_delete=models.PROTECT)
    data_zapisi = models.DateField(auto_now=True,unique=False,blank=True,verbose_name='Дата записи')
    coment = models.TextField(blank=True,verbose_name='Коментарий')
    class Meta:
        verbose_name='Запись на полеты'
        verbose_name_plural='Записи на полеты'
        ordering=['data_poleta']
    def __str__(self):
        datetimeObj=self.data_poleta.data
        dateStr=datetimeObj.strftime('%d-%b-%Y')
        return dateStr
