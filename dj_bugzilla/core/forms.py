from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields
from .models import Task, Ticket, ProjectManager, Developer, TaskPriority, TaskStatus


# assign_developers = Developer.objects.all().values_list('name','name')
# developer_list = []
# for item in assign_developers:
#     developer_list.append(item)


# priority_choices = TaskPriority.objects.all().values_list('name','name')
# priority_choice_list = []
# for item in priority_choices:
#     priority_choice_list.append(item)


# status_choices = TaskStatus.objects.all().values_list('name','name')
# status_choice_list = []
# for item in status_choices:
#     status_choice_list.append(item)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
           'description',
        #    'status',
        #    'priority',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',                            
                'placeholder':'title of your task',
                'id':"exampleFormControlInput77"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'add any extra details here',
                'id':"exampleFormControlTextarea78",
                'rows':"5"
                }
            ),
            # 'priority': forms.Select(choices=priority_choice_list, attrs={
            #     'class': 'form-control',
            #     'id':'formFileMultipleone',
            #     'aria-label':"Default select Priority",
            #     }
            # ),
            # 'status': forms.Select(choices=status_choice_list, attrs={
            #     'class': 'form-control',
            #     'id':'formFileMultiplestatus',
            #     'aria-label':"Default select Project Category",
            #     }
            # ),
        }


# class TaskEditForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = [
#             'title',
#            'description',
#            'status',
#            'priority',
#         ]

#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'form-control',                            
#                 'placeholder':'title of your task',
#                 'id':"exampleFormControlInput77"
#                 }
#             ),
#             'description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder':'add any extra details here',
#                 'id':"exampleFormControlTextarea78",
#                 'rows':"5"
#                 }
#             ),
#             'priority': forms.Select(choices=priority_choice_list, attrs={
#                 'class': 'form-control',
#                 'id':'formFileMultipleone',
#                 'aria-label':"",
#                 }
#             ),
#             'status': forms.Select(choices=status_choice_list, attrs={
#                 'class': 'form-control',
#                 'id':'formFileMultiplestatus',
#                 'aria-label':"",
#                 }
#             ),
#         }

##############################################################
# class AssignDeveloperForm(forms.ModelForm):
#     class Meta:
#         model  = Developer
#         fields = ['user']

#         widgets = {
#             'user': forms.Select(choices=developer_list, attrs={
#                 'class': 'form-control',
#                 'id':'formFileMultiplestatus',
#                 'aria-label':"Default select developer",
#                 }
#             ),
#         }



# class TicketForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = [
#             'title',
#             'description',
#             'priority',
#         ]

#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'form-control',                            
#                 'placeholder':'title of your task',
#                 'id':"exampleFormControlInput77"
#                 }
#             ),
#             'description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder':'add any extra details here',
#                 'id':"exampleFormControlTextarea78",
#                 'rows':"5"
#                 }
#             ),
#             'priority': forms.Select(choices=priority_choice_list, attrs={
#                 'class': 'form-control',
#                 'id':'formFileMultipleone',
#                 'aria-label':"Default select Priority",
#                 }
#             )
#         }