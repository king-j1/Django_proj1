from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Product


# -------------------------
# Registration Form
# -------------------------
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# -------------------------
# Client Form
# -------------------------
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "full_name", "email", "phone", "address",
            "city", "state", "country", "zip_code"
        ]


# -------------------------
# Product Form (FIXED)
# -------------------------
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "price", "description"]
