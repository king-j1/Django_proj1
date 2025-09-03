# webapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Import models and forms
from .models import Client, Product
from .forms import RegistrationForm, ClientForm, ProductForm


# -------------------------
# ADD PRODUCT
# -------------------------
@login_required
def add_product(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.client = client   # link product to client
            product.save()
            return redirect("client_products", client_pk=client.pk)
    else:
        form = ProductForm()

    return render(request, "add_product.html", {"form": form, "client": client})


# -------------------------
# HOME / LOGIN
# -------------------------
def home(request):
    """
    Home page: shows login form (POST) and client list (GET).
    """
    clients = Client.objects.all()

    # Handle login
    if request.method == "POST" and "username" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("home")

    return render(request, "home.html", {"clients": clients})


# -------------------------
# REGISTER
# -------------------------
def register_view(request):
    """Register a new user and log them in."""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in!")
            return redirect("home")
        messages.error(request, "There was a problem with your registration.")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})


# -------------------------
# LOGOUT
# -------------------------
def logout_view(request):
    """Log the user out and redirect to home."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


# -------------------------
# CLIENT CRUD
# -------------------------
@login_required(login_url="home")
def client_detail(request, client_pk):
    """Show a single client's details."""
    client = get_object_or_404(Client, pk=client_pk)
    return render(request, "client_detail.html", {"client": client})


@login_required(login_url="home")
def add_client(request):
    """Add a new client."""
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, "Client added successfully.")
            return redirect("client_detail", client_pk=client.pk)
        messages.error(request, "Please correct the errors below.")
    else:
        form = ClientForm()

    return render(request, "add_client.html", {"form": form})


@login_required(login_url="home")
def edit_client(request, client_pk):
    """Edit an existing client."""
    client = get_object_or_404(Client, pk=client_pk)

    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client updated successfully.")
            return redirect("client_detail", client_pk=client.pk)
        messages.error(request, "Please correct the errors below.")
    else:
        form = ClientForm(instance=client)

    return render(request, "edit_client.html", {"form": form, "client": client})


@login_required(login_url="home")
def delete_client(request, client_pk):
    """Delete a client."""
    client = get_object_or_404(Client, pk=client_pk)
    if request.method == "POST":
        client.delete()
        messages.success(request, "Client deleted successfully.")
        return redirect("home")
    return redirect("client_detail", client_pk=client_pk)


# -------------------------
# PRODUCT LIST FOR A CLIENT
# -------------------------
@login_required(login_url="home")
def client_products(request, client_pk):
    client_record = get_object_or_404(Client, pk=client_pk)
    products = client_record.products.all()
    return render(
        request,
        "product.html",
        {"client_record": client_record, "products": products},
    )
