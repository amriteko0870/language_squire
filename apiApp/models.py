from django.db import models

# Create your models here.

class user_login(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    phone_code = models.TextField()
    phone_no = models.TextField()
    age = models.TextField()
    gender = models.TextField()
    password = models.TextField()
    user_type = models.TextField() # s-> superadmin, a-> Admin, u -> User
    active_course = models.TextField(blank=True)
    payment_status = models.BooleanField()
    token = models.TextField()

class curriculum(models.Model):
    name = models.TextField(blank=False,null= False)

class set_of_test(models.Model):
    name = models.TextField()
    description = models.TextField()

class test_assigned(models.Model):
    user_id = models.TextField()
    set_of_test_id = models.TextField()
    completion_status = models.BooleanField(default=False)
    listening_score = models.TextField(blank=True)
    reading_score = models.TextField(blank=True)
    writing_score = models.TextField(blank=True)
    speaking_score = models.TextField(blank=True)
    writing_remarks = models.TextField(blank=True)
    speaking_remarks = models.TextField(blank=True)
    admin_check_status = models.BooleanField(default=False)