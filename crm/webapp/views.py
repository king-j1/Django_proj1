from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import RegistrationForm, ClientForm  # ✅ import ClientForm


def home(request):
    """
    Shows login form (if not authenticated) and the client table (if authenticated).
    Also handles POST login from this same page.
    """
    clients = Client.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        messages.error(request, "Invalid username or password.")
        return redirect("home")

    return render(request, "home.html", {"clients": clients})


@login_required(login_url="home")
def client_detail(request, pk):
    """
    Show full details for a single client.
    """
    client = get_object_or_404(Client, pk=pk)
    return render(request, "client_detail.html", {"client": client})


@login_required(login_url="home")
def edit_client(request, pk):
    """
    Edit an existing client using ClientForm.
    """
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client updated successfully.")
            return redirect("client", pk=client.pk)  # go back to client detail
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ClientForm(instance=client)

    return render(request, "edit_client.html", {"form": form, "client": client})


@login_required(login_url="home")
def delete_client(request, pk):
    """
    Delete a client safely (only via POST).
    """
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        messages.success(request, "Client deleted successfully.")
        return redirect("home")
    return redirect("client", pk=pk)


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in right after registration
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in!")
            return redirect("home")
        messages.error(request, "There was a problem with your registration.")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})
