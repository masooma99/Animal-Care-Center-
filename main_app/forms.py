from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Animal, Products, Appointment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.CharField()  # (max_length=255)
    clinic = forms.BooleanField()  # (default=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "image",
            "clinic",
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["product_name", "description", "image", "price"]


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["animal_name", "age", "image", "type"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["reason", "date", "time", "animal"]
