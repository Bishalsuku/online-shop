from django.urls import path
from .views import Login_views,user_logout



urlpatterns = [
    path('',Login_views,name='login'),
    path('out',user_logout,name='logout')
]
