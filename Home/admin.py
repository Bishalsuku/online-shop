from django.contrib import admin
from .models import item, cart, bought, trending

# Register your models here.
admin.site.register(item)
admin.site.register(cart)
admin.site.register(bought)
admin.site.register(trending)