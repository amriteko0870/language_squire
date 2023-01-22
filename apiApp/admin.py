from django.contrib import admin

from apiApp.models import user_login
from apiApp.models import curriculum
# Register your models here.

admin.site.register(user_login)
admin.site.register(curriculum)