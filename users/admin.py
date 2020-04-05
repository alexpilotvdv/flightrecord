from django.contrib import admin
from users.models import user
from users.models import flightday
from users.models import zapisi
# Register your models here.
admin.site.register(user)
admin.site.register(flightday)
admin.site.register(zapisi)
