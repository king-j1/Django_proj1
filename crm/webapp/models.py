from django.db import models
from django.db import models
from django.core.validators import MinValueValidator

# -------------------------
# Client Model
# -------------------------
class Client(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    # 👇 New field
    profile_photo = models.ImageField(
        upload_to="client_photos/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.full_name} - {self.email}"


# -------------------------
# Product Model
# -------------------------
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="products")
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True, null=True)  # ← added (or kept) description
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name



# -------------------------
# Service Model
# -------------------------
class Service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="services")
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_name} ({self.client.full_name})"


# -------------------------
# Order Model
# -------------------------
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    order_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_name} ({self.client.full_name})"


# -------------------------
# Invoice Model
# -------------------------
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="invoices")
    invoice_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_name} ({self.client.full_name})"


# -------------------------
# Payment Model
# -------------------------
class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="payments")
    payment_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_name} ({self.client.full_name})"


# -------------------------
# Customer Support Model
# -------------------------
class CustomerSupport(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="supports")
    support_name = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Support {self.support_name} ({self.client.full_name})"


# -------------------------
# Feedback Model
# -------------------------
class Feedback(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="feedbacks")
    feedback_name = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.feedback_name} ({self.client.full_name})"


# -------------------------
# Rental Model
# -------------------------
class Rental(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="rentals")
    rental_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rental {self.rental_name} ({self.client.full_name})"
    


# -------------------------
# ImageField to Client Model
# -------------------------
    

