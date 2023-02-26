from django.contrib import admin

from apiApp.models import user_login
from apiApp.models import curriculum
from apiApp.models import set_of_test
from apiApp.models import test_assigned
# Register your models here.

admin.site.register(user_login)
admin.site.register(curriculum)
admin.site.register(set_of_test)
admin.site.register(test_assigned)