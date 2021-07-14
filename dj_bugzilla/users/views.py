from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, View
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# from .forms import UserSignUpForm, LoginForm, AdminForm, PmForm, DevForm
from .forms import UserSignUpForm, LoginForm

from core.models import Administrator, BugUser,Developer, ProjectManager

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




class RoleView(View):
    def get(self, request, *args,**kwargs):
        non_dev = BugUser.objects.filter(is_developer=False)
        non_pm = BugUser.objects.filter(is_project_manager=False)
        non_admin = BugUser.objects.filter(is_superuser=False)
        context = {
            'non_dev' : non_dev,
            'non_pm' : non_pm,
            'non_admin' : non_admin
        }
        return render(request,'users/roles.html',context)

    def post(self, request, *args,**kwargs):
        if self.request.POST['ad'] != 'none':
            ad_id = self.request.POST['ad']
            
            user = BugUser.objects.get(id=ad_id)
            
            for item in Administrator.objects.all():
                if item != user.id:
                    user.is_superuser=True
                    user.save()

                    a_user = Administrator.objects.create(
                        username = user
                    )

                    return redirect('roles_home')

                
            return redirect('roles_home')


class PmPostView(View):
    def post(self, request, *args,**kwargs):
        if self.request.POST['pm'] != 'none':
            pm_id = self.request.POST['pm']
            user = BugUser.objects.get(id=pm_id)
            
            user.is_project_manager=True
            user.save()
            
            ad_user = self.request.user
            pm_user = Administrator.objects.get(username=ad_user)
            
            a_user = ProjectManager.objects.create(
                        username = user,
                        admin    = pm_user
                    )
            
            return redirect('roles_home')
        return redirect('roles_home')

class DevPostView(View):
    def post(self, request, *args,**kwargs):
        if self.request.POST['dev'] != 'none':
            dev_id = self.request.POST['dev']
            
            user = BugUser.objects.get(id=dev_id)
            user.is_developer=True
            user.save()
            
            dev_assigner = self.request.user
            assigner = BugUser.objects.get(id=dev_assigner.id)

            a_user = Developer.objects.create(
                        username = user,
                        assigner    = assigner
                    )
                    
            return redirect('roles_home')
        return redirect('roles_home')
   


    