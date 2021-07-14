import random

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


# Create your models here.
class BugUser(AbstractUser):
    is_developer       = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=False)

 
# class UserProfile(models.Model):
#     user = models.OneToOneField(BugUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username



# def create_userprofile_signal(sender,instance,created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# post_save.connect(create_userprofile_signal, sender=UserProfile)


class Administrator(models.Model):
    username = models.OneToOneField(BugUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username

    

class ProjectManager(models.Model):
    username  = models.OneToOneField(BugUser, on_delete=models.CASCADE)
    admin =  models.ForeignKey(Administrator,on_delete=models.SET_NULL, null=True,related_name='pm_assigner')

    def __str__(self):
        return self.username.username

    


class Developer(models.Model):
    username          = models.OneToOneField(BugUser, on_delete=models.CASCADE)
    assigner          = models.ForeignKey(BugUser,on_delete=models.SET_NULL, null=True,related_name='dev_assigner')
    

    def __str__(self):
        return self.username.username

class Task(models.Model):
    title              = models.CharField(max_length=255)
    description        = models.TextField()
    creator            = models.ForeignKey(BugUser,on_delete=models.SET_NULL, null=True,related_name='task_author')
    developer_assigned = models.ForeignKey(Developer,on_delete=models.SET_NULL, null=True,blank=True,related_name='task_developer')
    date_created       = models.DateField(auto_now_add=True)
    date_assigned      = models.DateField(auto_now=True)
    date_completed     = models.DateField(auto_now=True)
    status             = models.CharField(max_length=255)
    priority           = models.CharField(max_length=255)
    project            = models.CharField(max_length=255)
    

class TaskPriority(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class TaskStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


# class Project(models.Model):
#     title        = models.CharField(max_length=255)
#     description  = models.TextField()
#     creator      = models.ForeignKey(BugUser,on_delete=models.SET_NULL, null=True,related_name='project_creator')
#     status
#     date_created
#     begin_date
#     end_date
#     assigned_to  = pm


class Ticket(models.Model):
    ticket_id          = models.CharField(max_length=6, default='', unique=True)
    title              = models.CharField(max_length=150)
    description        = models.TextField()
    creator            = models.ForeignKey(BugUser,on_delete=models.SET_NULL, null=True,related_name='ticket_author')
    assigned_to        = models.ForeignKey(Developer,on_delete=models.SET_NULL, null=True,blank=True,related_name='ticket_developer')
    priority           = models.CharField(max_length=50)
    status             = models.CharField(max_length=50)
    # project            = models.CharField(max_length=50)
    date_created       = models.DateField(auto_now_add=True)
    date_resolved      = models.DateField(auto_now=True)
                 
   

class AllImage(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='img_ticket', on_delete=models.CASCADE,null=True)
    image  = models.ImageField(null=True, blank=True)


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket,related_name='ticket_comment',on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(BugUser,related_name='comment_author',on_delete=models.CASCADE,null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:10]
    
    



    

    




