from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from django.views.generic import CreateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path('accounts/', include('django.contrib.auth.urls')),
    url('^accounts/', include('django.contrib.auth.urls')),
    # path("accounts/signup", views.signup_view, name="signup"),
    url('^register/', CreateView.as_view(
        template_name='registration/registration_form.html',
        form_class=UserCreationForm,
        success_url='/'
    ), name="signup"),
    path("menu/", views.menu, name="menu"),
]
