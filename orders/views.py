from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


# Create your views here.
# def index(request):
#     return render(request, "product/list.html")  # index


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "categories": categories,
        "products": products
    }

    return render(request, "product/list.html", context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        "product": product,
        "cart_product_form": cart_product_form,
    }

    return render(request, "product/detail.html", context)


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
