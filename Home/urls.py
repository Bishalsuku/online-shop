from django.urls import path
from .views import (
    Home_views,
    Item,
    ItemDelete,
    ItemDetail,
    ItemUpdate,
    success,
    failed,
    boug,
)
from .views import (
    ItemCreate,
    addtocart,
    carts,
    CartDelete,
    itemlists,
    itemlist,
    about,
    contact,
    profile,
)

urlpatterns = [
    path("", Home_views),
    path("item/", itemlists, name="itemlist"),
    path("itemcreate/", ItemCreate.as_view(), name="itemcreate"),
    path("itemdetail/<int:pk>/", ItemDetail.as_view(), name="itemdetail"),
    path("itemdelete/<int:pk>/", ItemDelete.as_view(), name="itemdelete"),
    path("itemupdate/<int:pk>/", ItemUpdate.as_view(), name="itemupdate"),
    path("cartsdelete/<int:pk>/", CartDelete.as_view(), name="cartdelete"),
    path("itemslists/", itemlists, name="itemlists"),
    path("itemlist/<slug:slug>", itemlist, name="itemlisted"),
    path("addtocart/<int:pk>/", addtocart, name="addtocart"),
    path("carts/", carts, name="carts"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("profile/", profile, name="profile"),
    path("success/", success, name="success"),
    path("fail/", failed, name="failed"),
    path("bought/", boug, name="bought"),
]
