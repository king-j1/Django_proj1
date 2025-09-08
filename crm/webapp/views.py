from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Client
from .forms import ClientForm

# Import models and forms
from .models import Client, Product
from .forms import RegistrationForm, ClientForm, ProductForm


# -------------------------
# HOME (Dashboard + Login)
# -------------------------
def home(request):
    """Dashboard / home page (with login handling)."""
    clients = Client.objects.all()

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

    return render(request, "core/home.html", {"clients": clients})



# -------------------------
# AUTH
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

    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    """Log the user out and redirect to home."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


# -------------------------
# CLIENT CRUD
# -------------------------
@login_required(login_url="home")
def client_list(request):
    clients = Client.objects.all()
    return render(request, "clients/client_list.html", {"clients": clients})


@login_required(login_url="home")
def client_detail(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    return render(request, "clients/client_detail.html", {"client": client})


# -------------------------
# CLIENT ADD
# -------------------------
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm

@login_required(login_url="home")
def client_add(request):
    if request.method == "POST":
        # ✅ Don't use instance=client here, this is for new clients
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            messages.success(request, "Client added successfully.")
            return redirect("client_detail", client_pk=client.pk)
    else:
        form = ClientForm()

    return render(request, "clients/client_form.html", {"form": form})


@login_required(login_url="home")
def client_edit(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)

    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client updated successfully.")
            return redirect("client_detail", client_pk=client.pk)
    else:
        form = ClientForm(instance=client)

    return render(request, "clients/client_form.html", {"form": form, "client": client})


@login_required(login_url="home")
def client_delete(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    if request.method == "POST":
        client.delete()
        messages.success(request, "Client deleted successfully.")
        return redirect("client_list")

    return render(request, "clients/client_confirm_delete.html", {"client": client})



# -------------------------
# PRODUCT CRUD (per client)
# -------------------------
@login_required(login_url="home")
def product_list(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    products = client.products.all().order_by("-date")  # newest first

    # Pagination: show 10 products per page
    paginator = Paginator(products, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "products/product_list.html",
        {"client": client, "page_obj": page_obj},
    )


@login_required(login_url="home")
def product_detail(request, client_pk, pk):
    client = get_object_or_404(Client, pk=client_pk)
    product = get_object_or_404(Product, pk=pk, client=client)
    return render(
        request,
        "products/product_detail.html",
        {"client": client, "product": product},
    )


# -------------------------
# PRODUCT ADD
# -------------------------
@login_required
def product_add(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.client = client
            product.save()
            messages.success(request, "Product added successfully.")
            return redirect("product_list", client_pk=client.pk)
    else:
        form = ProductForm(request.POST, request.FILES)  
        return render(request, "products/product_form.html", {"form": form, "client": client})


@login_required
def product_edit(request, client_pk, pk):
    client = get_object_or_404(Client, pk=client_pk)
    product = get_object_or_404(Product, pk=pk, client=client)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect("product_detail", client_pk=client.pk, pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, "products/product_form.html", {"form": form, "client": client, "product": product})

# -------------------------
# INVOICES
# -------------------------
@login_required(login_url="home")
def invoice_list(request):
    return render(request, "invoices/invoice_list.html")


# -------------------------
# ORDERS
# -------------------------
@login_required(login_url="home")
def order_list(request):
    return render(request, "orders/order_list.html")


# -------------------------
# SERVICES
# -------------------------
@login_required(login_url="home")
def service_list(request):
    return render(request, "services/service_list.html")


# -------------------------
# RENTS
# -------------------------
@login_required(login_url="home")
def rent_list(request):
    return render(request, "rents/rent_list.html")


# -------------------------
# FEEDBACK
# -------------------------
@login_required(login_url="home")
def feedback_list(request):
    return render(request, "feedback/feedback_list.html")


# -------------------------
# PAYMENTS
# -------------------------
@login_required(login_url="home")
def payment_list(request):
    return render(request, "payments/payment_list.html")


# -------------------------
# PRODUCT DELETE
# -------------------------
@login_required(login_url="home")
def product_delete(request, client_pk, pk):
    client = get_object_or_404(Client, pk=client_pk)
    product = get_object_or_404(Product, pk=pk, client=client)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect("product_list", client_pk=client.pk)

    # If someone visits directly with GET, just redirect back
    return redirect("product_detail", client_pk=client.pk, pk=product.pk)



# -------------------------
# PRODUCT DELETE (with confirmation)
# -------------------------
@login_required(login_url="home")
def product_delete(request, client_pk, pk):
    client = get_object_or_404(Client, pk=client_pk)
    product = get_object_or_404(Product, pk=pk, client=client)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect("product_list", client_pk=client.pk)

    # Render confirmation page
    return render(
        request,
        "products/product_confirm_delete.html",
        {"client": client, "product": product},
    )

