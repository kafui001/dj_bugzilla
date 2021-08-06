from django.urls import path

from .views import  TaskView, TaskDetailView, TaskEditView, TaskDeleteView,DeleteNotification

app_name = 'core'

urlpatterns = [
    path('', TaskView.as_view(), name='task'),
    path('edit/<int:pk>/',TaskEditView.as_view(), name='task_edit'),
    path('delete/<int:pk>/',TaskDeleteView.as_view(), name='task_delete'),
    path('delete_notification/<int:pk>/',DeleteNotification.as_view(), name='notification_delete'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]