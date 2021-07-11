from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserSignUpForm, LoginForm, AdminForm, PmForm, DevForm
from core.models import Administrator, BugUser

class UserSignUpView(View):
    
    def get(self, request, *args, **kwargs):
        form = UserSignUpForm()
        return render(request, "users/signup.html", { 'form': form })

    def post(self, request, *args, **kwargs):

        form = UserSignUpForm(self.request.POST)

        if form.is_valid():
            # save the user form and log the user in
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.username = form.cleaned_data["username"]
            user.save()
            login(request, user)
            return redirect('core:task')
        else:
            return render(request, "users/signup.html", {
                'form': form
            })


class UserLogin(FormView):
    template_name = "users/signin.html"
    form_class = LoginForm
    success_url = reverse_lazy("core:task")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


# ROLES
# def roles(request):
#     context = {
#     }
#     return render(request, 'bug/roles.html',context)

class RoleView(CreateView):
    model         = Administrator
    form_class    = AdminForm
    template_name = 'users/roles.html'
    success_url = reverse_lazy('roles_home')

    def get_context_data(self, **kwargs):
        context = super(RoleView, self).get_context_data(**kwargs)
        context['pm_form'] = PmForm
        context['dev_form'] = DevForm
        return context

    def form_valid(self, form):
        user = form.instance.username
        print(user)
        user = BugUser.objects.filter(username=user)
        user.update(is_superuser=True)
    
        return super(RoleView, self).form_valid(form)
    