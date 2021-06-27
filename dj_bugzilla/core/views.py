from django.shortcuts import render
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import CreateView, FormView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm, TaskEditForm

#Create your views here.

# class TaskView(MultipleObjectMixin,FormView):
class TaskView(FormView):
    model = Task
    template_name = 'core/task.html'
    form_class = TaskForm
    success_url = reverse_lazy('core:task')
    # MultipleObjectMixin 
    # context_object_name = 'tasks'
    # paginate_by = 10
    # queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['unassigned'] = Task.objects.filter(status='open')
        context['in_progress'] = Task.objects.filter(status='in progress')
        context['needs_review'] = Task.objects.filter(status='needs review')
        context['completed'] = Task.objects.filter(status='completed')
        return context

#     # limit task creation to only admin and project manager
    def form_valid(self, form):
        form = form.save(commit=False)
        if self.request.user.is_project_manager or self.request.user.is_superuser:
            form.creator = self.request.user
            form.status = 'open'
            form.save()
            print(form.creator)
            print(form.priority)
            return super(TaskView, self).form_valid(form)
        else:
            print("you are not authorized to create a task")
#             # fix this section


class TaskDetailView(DetailView):
    model = Task
    # context_object_name = 'task'
    template_name = 'core/task_detail.html'


class TaskEditView(UpdateView):
    model = Task
    form_class = TaskEditForm
    template_name = 'core/task_edit.html'
    success_url = reverse_lazy('core:task')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'core/task_delete.html'
    success_url = reverse_lazy('core:task')