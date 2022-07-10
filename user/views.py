from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm, LoginForm


# redirect default request to login page
def redirectToUser(request):
    return redirect('/user')


# Class based view for the index page
class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            print("User is login Already")
            return redirect("bug_index")

        context = {
            "messages": messages.get_messages(request)
        }
        return render(request, 'login_templates/login_index.html', context)


# Register User
class Register(View):
    def post(self, request):
        form = UserForm(postRequest=request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                if User.objects.get(username=email):
                    messages.error(request, "User Already Exist", extra_tags="user_exist_error")
                    return redirect("index")
            except User.DoesNotExist:
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                password = form.cleaned_data.get("password")
                User.objects.create_user(username=email, email=email,
                                         password=password, first_name=first_name,
                                         last_name=last_name)

        return redirect("index")


class Login(View):
    def post(self, request):
        form = LoginForm(postRequest=request, data=request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data.get("email"), password=form.cleaned_data.get("password"))
            if user is not None:
                login(request, user)
                return redirect("bug_index")
            else:
                return render(request, "test_templates/test_failure.html")
        return render(request, "test_templates/test_failure.html")
