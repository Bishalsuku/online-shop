from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy
from .models import item, cart, bought, trending
from django.db.models import Q
from django.contrib import messages
from random import seed
from random import randint

seed(1)

# class based views
class ItemCreate(CreateView):
    model = item
    fields = ["name", "category", "user", "image", "description", "price"]
    template_name = "itemcreate.html"


class ItemUpdate(UpdateView):
    model = item
    fields = [
        "name",
        "description",
        "image",
        "price",
    ]
    template_name = "itemupdate.html"


class ItemDelete(DeleteView):
    model = item
    template_name = "itemdelete.html"
    success_url = reverse_lazy("itemlist")


class ItemDetail(DetailView):
    model = item
    template_name = "itemdetail.html"


class Item(ListView):
    context_object_name = "item_list"
    model = item
    template_name = "item.html"


class CartDelete(DeleteView):
    model = cart
    template_name = "cartdelete.html"
    success_url = reverse_lazy("carts")


def carts(request):
    random = randint(11111, 99999999)
    cartit = cart.objects.filter(user=request.user)
    cartCount = cart.objects.count()
    return render(
        request,
        "carts.html",
        {
            "carts": cartit,
            "random": random,
            "cartCount": cartCount,
        },
    )


# funtion based views
def addtocart(request, pk):
    new = cart(item=item.objects.get(id=pk), user=request.user)
    new.save()
    return redirect("/")


def itemlists(request):
    itemlist = item.objects.all()
    search_query = request.GET.get("q")
    count = item.objects.count()
    if search_query:
        itemlist = itemlist.filter(
            Q(name__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(category__icontains=search_query)
        )
    count2 = itemlist.count()
    return render(
        request,
        "item.html",
        {
            "item_list": itemlist,
            "search": search_query,
            "count": count,
            "count2": count2,
        },
    )


def itemlist(request, slug):
    itemlist = item.objects.all()
    itemlist = itemlist.filter(category=slug)
    return render(
        request,
        "item.html",
        {
            "item_list": itemlist,
            "slug": slug,
        },
    )


def Home_views(request):
    itemlist = item.objects.all()
    slides = trending.objects.all()
    random1 = randint(11111, 99999999)
    cartCount = cart.objects.count()
    return render(
        request,
        "home.html",
        {
            "item_list": itemlist[0:4],
            "items": itemlist[4:8],
            "slides": slides,
            "random1": random1,
            "cartCount": cartCount,
        },
    )


def about(request):
    return render(
        request,
        "about.html",
        {},
    )


def contact(request):
    return render(
        request,
        "contact.html",
        {},
    )


def profile(request):
    return render(
        request,
        "profile.html",
        {},
    )


def success(request):
    pk = request.GET.get("q")
    amt = request.GET.get("amt")
    refid = request.GET.get("refId")
    name = item.objects.get(id=pk)
    new = bought(item=item.objects.get(id=pk), user=request.user)
    new.save()
    messages.success(request, "You have purchased product " + name.name + "  ID " + pk)
    return redirect("/")


def failed(request):
    pk = request.GET.get("oid")
    amt = request.GET.get("amt")
    refid = request.GET.get("refId")
    return render(request, "failed.html", {"pk": pk, "amt": amt, "refid": refid})


def boug(request):
    boughtit = bought.objects.filter(user=request.user)
    return render(request, "bought.html", {"carts": boughtit})
