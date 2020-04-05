from django.contrib import admin
from users.models import user
from users.models import flightday
# Register your models here.
admin.site.register(user)
admin.site.register(flightday)
