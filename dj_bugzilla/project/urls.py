from django.urls import path


app_name = 'project'

from .views import ProjectHomeView

urlpatterns = [
    path('',ProjectHomeView.as_view(), name='project_home'),
    
]