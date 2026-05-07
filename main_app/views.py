from django.http import JsonResponse
from django.shortcuts import render, redirect

# from .models import User
# from .forms import SignUpUserForm, SignInUserForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


# Create your views here.
def intro_page(request):
    print(request.user)  # --> to check which user is logged in
    return render(request, "intro_page.html")


# -------------------------------------  auth  --------------------------------------------


from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):  # (CreateView):
    template_name = "registration/sign-up.html"
    form_class = CustomUserCreationForm
    success_url = "/auth/login"  # or your home


# -------------------------------------  profile page  --------------------------------------------
class UserDetailView(DetailView):
    model = CustomUser
    template_name = "user/user_detail.html"
    context_object_name = "user_details"
    pk_url_kwarg = "id"


class UserListView(ListView):
    model = CustomUser
    template_name = "user/user_list.html"
    context_object_name = "users"
    success_url = "/users/"
