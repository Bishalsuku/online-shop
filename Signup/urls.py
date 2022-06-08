from django.urls import path
from .views import Signup_views

urlpatterns = [
    path("", Signup_views, name="signup"),
]
