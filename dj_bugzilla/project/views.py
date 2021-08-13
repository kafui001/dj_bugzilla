from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView,FormView, DetailView, UpdateView, DeleteView,View
from core.mixins import SigninRequiredMixin, HigherLevelMixin

# Create your views here.
from .forms import ProjectForm, ProjectEditForm
from core.models import Ticket, Developer, AllImage, Comment,Notification,Administrator,Project,ProjectManager,Task
# from users.forms import DevTicketForm

# Create your views here.

class ProjectHomeView(SigninRequiredMixin,ListView):
    model               = Project
    template_name       = 'project/project.html'
    context_object_name = 'project'
    ordering            = ['-date_created']
    paginate_by         = 6

    def get_context_data(self, **kwargs):
        context              = super(ProjectHomeView, self).get_context_data(**kwargs)
        context['form']      = ProjectForm()
        context['edit_form'] = ProjectEditForm()
        return context


# incoming 'POST' info from project creation form in project.html
class ProjectFormView(FormView):
    model       = Project
    form_class  = ProjectForm
    success_url = reverse_lazy('project:project_home')

    def form_valid(self, form):
        form         = ProjectForm(self.request.POST)
        user = self.request.user
        admin_user = Administrator.objects.get(username=user)
       
        form         = form.save(commit=False)
        form.creator = admin_user
        form.status  = 'Drafted'
        form.completion = 0

        form.save()
        
        administrators = Administrator.objects.all()

        # loop through administrators to create notification for each admin about 
        # new ticket instance creation
        for admin in administrators:
            Notification.objects.create(
                notification_type = 3,
                to_user           = admin.username,
                from_user         = self.request.user,
                project           = form
            )

        return super(ProjectFormView, self).form_valid(form)


class ProjectEditView(SigninRequiredMixin,HigherLevelMixin,UpdateView):
    model         = Project
    form_class    = ProjectEditForm
    template_name = 'project/project_edit.html'

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.kwargs['pk']})


class ProjectDeleteView(SigninRequiredMixin,HigherLevelMixin,DeleteView):
    model               = Project
    context_object_name = 'project'
    template_name       = 'project/project_delete.html'
    success_url         = reverse_lazy('project:project_home')


class ProjectDetailView(SigninRequiredMixin,DetailView):
    model               = Project
    context_object_name = 'project'
    template_name       = 'project/project_detail.html'

    
    def get_context_data(self,**kwargs):

        # project_pk = {'pk': self.kwargs['pk']}
        # pk = [value for value in project_pk.values()][0]

        context                 = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['assign_pm']    = ProjectManager.objects.all()
        context['task']         = Task.objects.filter(project=self.kwargs['pk'])
        context['ticket']       = Ticket.objects.filter(project=self.kwargs['pk'])
        return context


class AssignProjectView(SigninRequiredMixin,View):
    def post(self, request, *args,**kwargs):
        if self.request.POST['pm'] != 'none':
            project_id = self.kwargs['pk']
            pm_id = self.request.POST['pm']
            
            pm = ProjectManager.objects.get(id=pm_id)
            

            project_instance = Project.objects.get(id=project_id)
            project_instance.project_lead = pm
            project_instance.save(update_fields=['project_lead'])

            Notification.objects.create(
                notification_type = 9,
                to_user           = pm.username,
                from_user         = self.request.user,
                project           = project_instance
            )
    
            return redirect(reverse('project:project_detail', kwargs={'pk': self.kwargs['pk']}))