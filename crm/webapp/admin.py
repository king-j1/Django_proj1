from django.contrib import admin
from .models import (
    Client, Product, Service, Order, Invoice,
    Payment, CustomerSupport, Feedback, Rental
)


# -------------------------
# Client Admin
# -------------------------
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "created_at")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("city", "state", "country", "created_at")
    ordering = ("-created_at",)


# -------------------------
# Product Admin
# -------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "client", "price", "date")
    search_fields = ("product_name", "client__full_name")
    list_filter = ("date",)


# -------------------------
# Service Admin
# -------------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name", "client", "price", "date")
    search_fields = ("service_name", "client__full_name")
    list_filter = ("date",)


# -------------------------
# Order Admin
# -------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_name", "client", "price", "date")
    search_fields = ("order_name", "client__full_name")
    list_filter = ("date",)


# -------------------------
# Invoice Admin
# -------------------------
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_name", "client", "price", "date")
    search_fields = ("invoice_name", "client__full_name")
    list_filter = ("date",)


# -------------------------
# Payment Admin
# -------------------------
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_name", "client", "price", "date")
    search_fields = ("payment_name", "client__full_name")
    list_filter = ("date",)


# -------------------------
# Customer Support Admin
# -------------------------
@admin.register(CustomerSupport)
class CustomerSupportAdmin(admin.ModelAdmin):
    list_display = ("support_name", "client", "date")
    search_fields = ("support_name", "client__full_name")
    list_filter = ("date",)


# -------------------------
# Feedback Admin
# -------------------------
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("feedback_name", "client", "date")
    search_fields = ("feedback_name", "client__full_name")
    list_filter = ("date",)


# -------------------------
# Rental Admin
# -------------------------
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ("rental_name", "client", "price", "date")
    search_fields = ("rental_name", "client__full_name")
    list_filter = ("date",)
