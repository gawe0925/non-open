from django.urls import path
from shop.views import *
from store import settings
import static


urlpatterns = [
    path('', store, name="Store"),
    path('cart/', cart, name="Cart"),
    path('checkout/', checkout, name="Checkout"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('payout/', payout, name="payout"),
    path('update_item/', updateItem, name="update_item")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)