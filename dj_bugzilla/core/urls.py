from django.urls import path

# from .views import  TaskView, TaskDetailView, TaskEditView, TaskDeleteView
from .views import  TaskView
app_name = 'core'

urlpatterns = [
    path('', TaskView.as_view(), name='task'),
    # path('roles/',roles, name='roles_home'),
    # path('edit/<int:pk>/',TaskEditView.as_view(), name='task_edit'),
    # path('delete/<int:pk>/',TaskDeleteView.as_view(), name='task_delete'),
    # path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]