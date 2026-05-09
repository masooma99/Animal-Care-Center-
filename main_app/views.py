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
    pk_url_kwarg = id


# class ProductCreateView(CreateView):
#     model = Products
#     form_class = ProductForm
#     success_url = "/product/create/"
#     template_name = "user/clinic_form/create_product.html"


# def create_product(request, id):
#     print(request.method)
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()  # (commit=False)
#             # product.clinic = id
#             # product.save()
#             # return redirect("/")
#         form = ProductForm()
#         return render(
#             request, "user/clinic_profile/clinic_product_list.html", {"product": product}
#         )
# Function-based view approach
def create_product(request, id):
    # print(type(request.user.id))
    user_id = str(request.user.id)
    print(user_id)
    print(type(user_id))
    # print(request.user)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  # In-memory creation
            product.clint = id  # Set user
            product.save()  # Commit
            # it does not do any of there thing but it does create the product
            return render(
                request,
                "user_detail.html",
                {"product": product},
            )
    form = ProductForm()
    return redirect("/users/{user_id}")
    # return render(request, "user/clinic_form/create_product.html", {"form": form})


# -------------------------------------  Animals  --------------------------------------------


class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = "animal/create"
    template_name = "user/clinic_form/create_animal.html"
