from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Product


# Create your views here.
def index(request):
    return render(request, "index.html")


def menu(request):
    menu_items = Product.objects.all()

    return render(request, "menu.html", {
        "pizza_regular": menu_items.filter(type="pizza_regular"),
        "pizza_sicilian": menu_items.filter(type="pizza_sicilian"),
        "toppings": menu_items.filter(type="toppings"),
        "subs": menu_items.filter(type="subs"),
        "pasta": menu_items.filter(type="pasta"),
        "salads": menu_items.filter(type="salads"),
        "dinner_platters": menu_items.filter(type="dinner_platters"),
    })


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
