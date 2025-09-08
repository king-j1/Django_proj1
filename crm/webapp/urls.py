from django.urls import path
from . import views

urlpatterns = [
    # -------------------------
    # Home / Auth
    # -------------------------
    path("", views.home, name="home"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    # -------------------------
    # Clients
    # -------------------------
    path("clients/", views.client_list, name="client_list"),
    path("clients/add/", views.client_add, name="client_add"),
    path("clients/<int:client_pk>/", views.client_detail, name="client_detail"),
    path("clients/<int:client_pk>/edit/", views.client_edit, name="client_edit"),
    path("clients/<int:client_pk>/delete/", views.client_delete, name="client_delete"),

    # -------------------------
    # Products (per client)
    # -------------------------
    path("<int:client_pk>/products/", views.product_list, name="product_list"),
    path("<int:client_pk>/products/add/", views.product_add, name="product_add"),
    path("<int:client_pk>/products/<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:client_pk>/products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("<int:client_pk>/products/<int:pk>/delete/", views.product_delete, name="product_delete"),

    # -------------------------
    # Invoices
    # -------------------------
    path("invoices/", views.invoice_list, name="invoice_list"),

    # -------------------------
    # Orders
    # -------------------------
    path("orders/", views.order_list, name="order_list"),

    # -------------------------
    # Services
    # -------------------------
    path("services/", views.service_list, name="service_list"),

    # -------------------------
    # Rents
    # -------------------------
    path("rents/", views.rent_list, name="rent_list"),

    # -------------------------
    # Feedback
    # -------------------------
    path("feedback/", views.feedback_list, name="feedback_list"),

    # -------------------------
    # Payments
    # -------------------------
    path("payments/", views.payment_list, name="payment_list"),
]
