from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ProductForm, AnimalForm
from .models import Products, Animal

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
    print(request.user.id)  # --> to check which user is logged in
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
    template_name = "user_detail.html"
    context_object_name = "user_details"
    pk_url_kwarg = "id"


# -------------------------------------  home page  --------------------------------------------


class UserListView(ListView):
    model = CustomUser
    template_name = "homepage.html"
    context_object_name = "users"
    success_url = "/users/"


# -------------------------------------  Products  --------------------------------------------


class ProductListView(ListView):
    model = Products
    template_name = "clinic_products_list.html"
    context_object_name = "products"
    success_url = "/users/{id}/product/"

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.kwargs.get("id"))

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx


def create_product(request, id):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  # In-memory creation
            product.clinic = request.user  # Set user
            product.save()  # Commit
            # it does not do any of there thing but it does create the product
            # return render(
            #     request,
            #     "user_detail.html",
            #     {"product": product},
            # )
            return redirect(f"/users/{request.user.id}")
    form = ProductForm()
    # return redirect("/users/{request.user}")
    return render(request, "user/clinic_form/create_product.html", {"form": form})


# -------------------------------------  Animals  --------------------------------------------


def create_animal(request, id):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)  # In-memory creation
            animal.clinic = request.user  # Set user
            animal.save()  # Commit
            # it does not do any of there thing but it does create the product
            # return render(
            #     request,
            #     "user_detail.html",
            #     {"product": product},
            # )
            return redirect(f"/users/{request.user.id}")
    form = AnimalForm()
    # return redirect("/users/{request.user}")
    return render(request, "user/clinic_form/create_animal.html", {"form": form})


class AnimalListView(ListView):
    model = Animal
    template_name = "user/clinic_profile/animal_list.html"
    context_object_name = "animals"
    success_url = "/users/{id}/animal/"

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.kwargs.get("id"))

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx


# -------------------------------------  Appointment  --------------------------------------------


def create_appointment(request, id):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)  # In-memory creation
            animal.clinic = request.user  # Set user
            animal.save()  # Commit
            # it does not do any of there thing but it does create the product
            # return render(
            #     request,
            #     "user_detail.html",
            #     {"product": product},
            # )
            return redirect(f"/users/{request.user.id}")
    form = AnimalForm()
    # return redirect("/users/{request.user}")
    return render(request, "user/clinic_form/create_animal.html", {"form": form})


class AppointmentListView(ListView):
    model = Animal
    template_name = "user/clinic_profile/animal_list.html"
    context_object_name = "animals"
    success_url = "/users/{id}/animal/"

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.kwargs.get("id"))

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx
