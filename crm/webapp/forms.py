from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
            "city", "state", "country", "zip_code",
            "profile_photo",  # 👈 added here
        ]


# -------------------------
# Product Form (with Image)
# -------------------------
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_code", "price", "description", "image"]

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
