from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Animal, Products, Appointment


class CustomUserCreationForm(UserCreationForm):
    image = forms.CharField()
    clinic = forms.BooleanField(required=False, initial=False)
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "image",
            "clinic",
            "email",
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
