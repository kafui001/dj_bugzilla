from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import CreateView, FormView, DetailView, UpdateView, DeleteView,View
from django.urls import reverse_lazy

from .models import Task,Notification
from .forms import TaskForm, TaskEditForm

#Create your views here.

# class TaskView(MultipleObjectMixin,FormView):
class TaskView(FormView):
    model = Task
    template_name = 'core/task.html'
    form_class = TaskForm
    success_url = reverse_lazy('core:task')

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

            # send task creation notification to assigned pm
            # Notification.objects.create(
            #         notification_type = 2,
            #         to_user           = dev.username,
            #         from_user         = self.request.user,
            #         task            = form
            #     )

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


class DeleteNotification(DeleteView):
    model = Notification

    def post(self, request, pk,*args,**kwargs):

        print('##########')
        print('getting somewhere')
        print('##########')
        notification = Notification.objects.get(id=pk)

        if notification.notification_type == 1:
            tic_id = notification.ticket.id
            notification.delete()
            print('##########')
            print('notification deleted')
            print('##########')
            return redirect(reverse('ticket:ticket_detail', kwargs={'pk': tic_id}))
        elif notification.notification_type == 4:
            dev_role = notification.dev_role_assign.id
            notification.delete()
            return redirect('assign_dev_role')
        elif notification.notification_type == 5:
            notification.delete()
            print('##########')
            print('notification type 5 deleted')
            print('##########')
            return redirect('assign_pm_role')
        elif notification.notification_type == 6:
            notification.delete()
            print('##########')
            print('notification type 6 deleted')
            print('##########')
            return redirect('assign_admin_role')
        elif notification.notification_type == 7:
            tic_id = notification.ticket.id
            notification.delete()
            print('##########')
            print('notification type 7 deleted')
            print('##########')
            # return redirect('assigned_role', kwargs={'pk': tic_id})
            # return redirect(reverse('assigned_role', kwargs={'pk': tic_id}))
            return redirect(reverse('ticket:assigned_to', kwargs={'pk': tic_id}))

