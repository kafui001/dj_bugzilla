import random

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView

from .forms import TicketForm, TicketEditForm
from core.models import Ticket, Developer, AllImage, TicketImage
from users.forms import DevTicketForm
# Create your views here.

class TicketHomeView(ListView):
    model               = Ticket
    template_name       = 'ticket/ticket.html'
    context_object_name = 'tickets'
    ordering            = ['-date_created']
    paginate_by         = 6

    def get_context_data(self, **kwargs):
        context         = super(TicketHomeView, self).get_context_data(**kwargs)
        context['form'] = TicketForm()
        return context

# 'POST' info from ticket creation form from ticket.html
class TicketFormView(FormView):
    model       = Ticket
    form_class  = TicketForm
    success_url = reverse_lazy('ticket:ticket_home')

    def form_valid(self, form):
        form         = TicketForm(self.request.POST)
        new_image    = self.request.FILES.get('image')
        print('#########')
        print(new_image)
        print('#########')
        form         = form.save(commit=False)
        form.creator = self.request.user
        form.status  = 'open'

        # create a ticket number for ticket instance
        while True:
            id = random.randint(10000,99999)
            if Ticket.objects.filter(ticket_id=id).count() == 0:
                break 
        form.ticket_id = id 
        
        save_new_image = AllImage.objects.create(
            image = new_image
        )
        form.save()

        new_ticketImage = TicketImage.objects.create(ticket=form,allimage=save_new_image,)

        return super(TicketFormView, self).form_valid(form)
 
class TicketDetailView(DetailView):
    model               = Ticket
    template_name       = 'ticket/ticket_detail.html'
    context_object_name = 'ticket'

    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        context['form'] = DevTicketForm()
        context['image'] = Ticket.tickets.values()
        return context


class TicketEditView(UpdateView):
    model         = Ticket
    form_class    = TicketEditForm
    template_name = 'ticket/ticket_edit.html'
    success_url   = reverse_lazy('ticket:ticket_home')

class TicketDeleteView(DeleteView):
    model               = Ticket
    context_object_name = 'ticket'
    template_name       = 'ticket/ticket_delete.html'
    success_url         = reverse_lazy('ticket:ticket_home')