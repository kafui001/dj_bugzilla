from django.shortcuts import render
from django.views.generic import ListView, CreateView,FormView, DetailView, UpdateView, DeleteView,View

# Create your views here.
from .forms import ProjectForm
from core.models import Ticket, Developer, AllImage, Comment,Notification,Administrator,Project
# from users.forms import DevTicketForm

# Create your views here.

class ProjectHomeView(ListView):
    model               = Project
    template_name       = 'project/project.html'
    context_object_name = 'project'
    ordering            = ['-date_created']
    paginate_by         = 6

    def get_context_data(self, **kwargs):
        context         = super(ProjectHomeView, self).get_context_data(**kwargs)
        context['form'] = ProjectForm()
        return context