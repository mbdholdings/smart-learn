from distutils.command.upload import upload
import email
import os
from random import choices
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse


def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    #get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)


class UserProfileInfo(models.Model):
    id = models.AutoField(primary_key=True)
    #Creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.TextField(max_length=500, blank=True, null=True)
    role = models.CharField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True, null=True)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
        
class Slide(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    motto = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Welcome(models.Model):
    id = models.AutoField(primary_key=True)
    title1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    motto = models.CharField(max_length=500, blank=True, null=True)
   

    def __str__(self):
        return self.motto

class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    def __str__(self):
        return self.subject

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    def __str__(self):
        return self.subject