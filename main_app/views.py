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


# def my_view(request):
#     data = list(User.objects.values())
#     return render(request, "user/sign_up.html", {"table_data": data})


# def get_data(request):
#     data = list(User.objects.values())  # Get database records
#     return JsonResponse(data, safe=False)


# class signUpCreateView(CreateView):
#     model = User
#     form_class = SignUpUserForm
#     success_url = "/"
#     template_name = "user/sign_up.html"

#     def form_valid(self, form):
#         return super().form_valid(form)


# class signInCreateView(CreateView):
#     model = User
#     form_class = SignInUserForm
#     success_url = "/"
#     template_name = "user/sign_in.html"


from django.contrib.auth.forms import UserCreationForm


class SignUpView2(CreateView):
    template_name = "registration/sign-up.html"
    form_class = UserCreationForm
    success_url = "/auth/login"  # or your home


# 1. password and confirm password have to match
# 2. email needs the @
# 3.
