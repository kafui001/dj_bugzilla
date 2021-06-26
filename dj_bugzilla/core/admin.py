from django.contrib import admin
from .models import Task,BugUser,TaskStatus,TaskPriority
# # Register your models here.

admin.site.register(BugUser)
admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(TaskPriority)