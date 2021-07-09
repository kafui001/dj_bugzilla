import random

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView

from .forms import TicketForm, TicketEditForm, CommentForm
from core.models import Ticket, Developer, AllImage, Comment
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
        form.save()

        save_new_image = AllImage.objects.create(
            ticket = form,
            image = new_image
        )
        # save_new_image.ticket.add(form)
        # new_ticketImage = TicketImage.objects.create(ticket=form,allimage=save_new_image,)

        return super(TicketFormView, self).form_valid(form)
 
class TicketDetailView(DetailView):
    model               = Ticket
    template_name       = 'ticket/ticket_detail.html'
    context_object_name = 'ticket'

    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        context['form']         = DevTicketForm()
        context['comment_form'] = CommentForm()
        context['image']        = AllImage.objects.all()
        context['all_comments'] = Comment.objects.all()
        return context

# class CommentFormWork(FormView):
#     model       = Comment
#     form_class  = CommentForm
#     # success_url = reverse_lazy('ticket:ticket_detail')
#     def get_success_url(self):
#         return reverse('ticket:ticket_detail', kwargs={'pk': self.object.pk})

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form) 



#     def form_valid(self, form):
#         form        = form.save(commit=False)
#         form.author = self.request.user
#         form.save()

#         return super(TicketDetailView, self).form_valid(form)


# class ViewPhoto(DetailView):
#     model               = AllImage
#     template_name       = 'ticket/image.html'
#     context_object_name = 'photo'

    # def get_context_data(self, **kwargs):
    #     context          = super(ViewPhoto, self).get_context_data(**kwargs)
    #     context['photo'] = AllImage.objects.get(id=self.id)
    #     return context

# class ViewImage(DetailView):
#     model               = AllImage
#     template_name       = 'ticket/image.html'

#     def get_context_data(self, **kwargs):
#         id = self.request.GET.get('name')
#         context = super(ViewImage, self).get_context_data(**kwargs)
#         context['image'] = AllImage.objects.get(id=id)
#         # context['image'] = AllImage.objects.all()
#         return context


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