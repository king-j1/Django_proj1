# webapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage (list + login)

    # Client routes
    path("client/<int:client_pk>/", views.client_detail, name="client_detail"),
    path("client/<int:client_pk>/edit/", views.edit_client, name="edit_client"),
    path("client/<int:client_pk>/delete/", views.delete_client, name="delete_client"),
    path("client/add/", views.add_client, name="add_client"),

    # Product routes
    path("client/<int:client_pk>/products/", views.client_products, name="client_products"),
    path("client/<int:client_pk>/products/add/", views.add_product, name="add_product"),

    # Authentication routes
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]
