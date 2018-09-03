from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["password"]
        first_name = request.POST["password"]
        last_name = request.POST["password"]

        # Create user and save to the database
        user = User.objects.create_user(username, email, password, first_name, last_name)
        user.save()

    return render(request, "registration/signup.html", {"message": "Create new account"})

# def login_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "registration/login.html", {"message": "Invalid credentials."})
#
#
# def logout_view(request):
#     logout(request)
#     return render(request, "registration/login.html", {"message": "Logged out."})
