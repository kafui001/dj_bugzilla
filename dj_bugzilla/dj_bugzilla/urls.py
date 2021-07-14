
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView

from users import views as user_views
# from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.UserSignUpView.as_view(), name='signup'),
    path('', user_views.UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # connecting roles and dashboard page directly for a more direct URL
    path('roles/',user_views.RoleView.as_view(), name='roles_home'),
    path('assign_pm/',user_views.PmPostView.as_view(), name='pm_role'),
    path('assign_dev/',user_views.DevPostView.as_view(), name='dev_role'),
    
    # path('dashboard/',core_views.dashboard, name='dashboard_home'),

    path('task/',include('core.urls', namespace='core')),
    path('ticket/',include('ticket.urls', namespace='ticket')),
    # path('project/',include('project.urls', namespace='project')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
