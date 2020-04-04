from django.db import models

# Create your models here.
class user(models.Model):
    foto = models.ImageField('Фото',upload_to='users/foto',default='',blank=True)
    nik = models.CharField(max_length=15,verbose_name='Ник')
    firstname = models.CharField(max_length=15,verbose_name='Имя')
    lastname = models.CharField(max_length=15,verbose_name='Фамилия')
    pfone = models.CharField(max_length=12,blank=True,verbose_name='Телефон')
    dborn = models.DateField(auto_now=False,auto_now_add=False,blank=True,verbose_name='Дата рождения')
    email = models.EmailField(max_length=50,blank=True,verbose_name='Email')
    rate = models.IntegerField(default=0,verbose_name='Рейтинг')
    class meta:
        verbose_name='Член клуба'
        verbose_name_plural='Члены клуба'
        ordering=['lastname']
    def __str__(self):
        return self.lastname
        
