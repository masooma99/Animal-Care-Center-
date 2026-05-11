from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ProductForm, AnimalForm, AppointmentForm
from .models import Products, Animal, Appointment, Order

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

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.kwargs.get("id"))

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx


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
    if id != request.user.id:
        return redirect("/")
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  # In-memory creation
            product.clinic = request.user  # Set user
            # if request.user.id == id:
            product.save()
            return redirect(f"/users/{request.user.id}")
    form = ProductForm()
    # return redirect("/users/{request.user}")
    return render(request, "user/clinic_form/create_product.html", {"form": form})


# -------------------------------------  Animals  --------------------------------------------


def create_animal(request, id):
    if id != request.user.id:
        return redirect("/")
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


class AnimalDetailView(DetailView):
    model = Animal
    template_name = "user/clinic_profile/Animal_detail.html"
    context_object_name = "animal_details"
    pk_url_kwarg = "animal_id"


def adopt_animal(request, id, animal_id):

    animal_details = Animal.objects.get(id=animal_id)
    if not animal_details.owner:
        animal_details.owner = request.user
        animal_details.save()
    return redirect(f"/users/{id}/animal")
    # ctx = super().get_context_data(**kwargs)
    # ctx["animal_details"] = animal_details
    # return ctx


# -------------------------------------  Appointment  --------------------------------------------


def create_appointment(request, id):
    clinic_user = CustomUser.objects.get(id=id)
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        form.fields["animal"].queryset = Animal.objects.filter(owner=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.owner = request.user
            appointment.clinic = clinic_user
            if appointment.reason == "Shower":
                appointment.price = 2
            elif appointment.reason == "Nail Care":
                appointment.price = 3
            else:
                appointment.price = 8
            appointment.save()
            return redirect(f"/users/{request.user.id}")
    else:
        form = AppointmentForm()
        form.fields["animal"].queryset = Animal.objects.filter(owner=request.user)
    return render(request, "user/clinic_form/create_appointment.html", {"form": form})


#  clinic appointments
class ClinicAppointmentListView(ListView):
    model = Appointment
    template_name = "user/clinic_profile/clinic_appointments.html"
    context_object_name = "appointments"
    success_url = "/users/{id}/appointment/"

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.kwargs.get("id"))

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx


#  normal user appointments
class AppointmentListView(ListView):
    model = Appointment
    template_name = "user/profile/pet_appointment_list.html"
    context_object_name = "pet_appointments"
    success_url = "/users/{id}/appointments/"

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.request.user.id)

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx


class AppointmentListView(ListView):
    model = Appointment
    template_name = "user/profile/pet_appointment_list.html"
    context_object_name = "pet_appointments"
    success_url = "/users/{id}/appointments/"

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.request.user.id)

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx


def pet_list(request, id):
    user_details = CustomUser.objects.get(id=id)
    user_pets = Animal.objects.filter(owner=user_details)
    print(user_details)
    print(user_pets)
    return render(
        request,
        "user/profile/pet_list.html",
        {"user_details": user_details, "pets": user_pets},
    )


# class PetListView(ListView):
#     model = Animal
#     template_name = "user/profile/pet_list.html"
#     context_object_name = "pets"
#     success_url = "/users/{id}/pet/"

#     def get_context_data(self, **kwargs):
#         user_details = CustomUser.objects.get(id=self.request.user.id)

#         ctx = super().get_context_data(**kwargs)
#         ctx["user_details"] = user_details
#         return ctx


class OrderListView(ListView):
    model = Order
    template_name = "user/profile/order_list.html"
    context_object_name = "orders"
    success_url = "/users/{id}/order/"

    def get_context_data(self, **kwargs):
        user_details = CustomUser.objects.get(id=self.request.user.id)

        ctx = super().get_context_data(**kwargs)
        ctx["user_details"] = user_details
        return ctx


class productDetailView(DetailView):
    model = Products
    template_name = "user/clinic_profile/product_detail.html"
    context_object_name = "product_details"
    pk_url_kwarg = "product_id"


# ===============================  Shopping  =========================================
