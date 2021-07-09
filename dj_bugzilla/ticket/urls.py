from django.urls import path

from .views import TicketHomeView, TicketFormView, TicketDetailView, TicketEditView, TicketDeleteView


app_name = 'ticket'

urlpatterns = [
    path('',TicketHomeView.as_view(), name='ticket_home'),
    path('detail/<int:pk>/',TicketDetailView.as_view(), name='ticket_detail'),
    path('edit/<int:pk>/',TicketEditView.as_view(), name='ticket_edit'),
  
    path('delete/<int:pk>/',TicketDeleteView.as_view(), name='ticket_delete'),
    path('ticket_form/',TicketFormView.as_view(), name='ticket_form'),
]