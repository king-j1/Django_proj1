from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check the login user
    if request.method == "POST":  # ✅ must be uppercase
        username = request.POST.get("username")  # ✅ must be POST
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")  # redirect after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("home")
    
    # GET request → just show the login form
    return render(request, "home.html", {})



def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


