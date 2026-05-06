from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpUserForm, SignInUserForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


# Create your views here.
def intro_page(request):
    return render(request, "intro_page.html")


# -------------------------------------  auth  --------------------------------------------


def my_view(request):
    data = list(User.objects.values())
    return render(request, "user/sign_up.html", {"table_data": data})


class signUpCreateView(CreateView):
    model = User
    form_class = SignUpUserForm
    success_url = "/"
    template_name = "user/sign_up.html"


class signInCreateView(CreateView):
    model = User
    form_class = SignInUserForm
    success_url = "/"
    template_name = "user/sign_in.html"
