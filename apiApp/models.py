from datetime import datetime
import pytz
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
    batch_id = models.TextField(default='u')
    active_course = models.TextField(blank=True)
    payment_status = models.BooleanField()
    date_time = models.TextField(default=str(datetime.now(pytz.timezone("Asia/Kolkata"))))
    token = models.TextField()

class batch_creation(models.Model):
    date_time = models.TextField(default=str(datetime.now(pytz.timezone("Asia/Kolkata"))))
    student_count = models.TextField(default='0')
    assignment_array = models.TextField(default='[]')

class curriculum(models.Model):
    name = models.TextField(blank=False,null= False)

class set_of_test(models.Model):
    name = models.TextField()
    description = models.TextField()

class test_assigned(models.Model):
    user_id = models.TextField()
    set_of_test_id = models.TextField()
    listening_status = models.BooleanField(default=False)
    reading_status = models.BooleanField(default=False)
    writing_status = models.BooleanField(default=False)
    speaking_status = models.BooleanField(default=False)
    listening_score = models.TextField(blank=True)
    reading_score = models.TextField(blank=True)
    writing_score = models.TextField(blank=True)
    speaking_score = models.TextField(blank=True)
    listening_answers = models.TextField(blank=True)
    reading_answers = models.TextField(blank=True)
    writing_answers = models.TextField(blank=True)
    speaking_answers = models.TextField(blank=True)
    writing_remarks = models.TextField(blank=True)
    speaking_remarks = models.TextField(blank=True)
    completion_status = models.BooleanField(default=False)
    admin_check_status = models.BooleanField(default=False)