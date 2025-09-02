
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),                          # list + login on the same page
    path("client/<int:pk>/", views.client_detail, name="client"),  # detail page
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("client/<int:pk>/edit/", views.edit_client, name="edit_client"),
    path("client/<int:pk>/delete/", views.delete_client, name="delete_client"),

]
