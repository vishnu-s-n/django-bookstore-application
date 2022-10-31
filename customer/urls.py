from django.urls import path
from customer import views

urlpatterns = [
    path("",views.LoginView.as_view(),name="login"),
    path("register",views.RegistrationView.as_view(),name="registration"),
    path("home",views.HomeView.as_view(),name="home"),
    path("book/<int:id>",views.BookDetailView.as_view(),name="book-detail"),
    path("products/<int:id>/carts/add",views.AddtoCart.as_view(),name="addto-cart"),
    path("carts/all",views.MyCartView.as_view(),name="mycart"),
    path("carts/remove/<int:id>",views.cart_item_remove,name="removeitem"),
    path("carts/placeorder/<int:cid>/<int:pid>",views.PlaceOrderView.as_view(),name="place-order")

]