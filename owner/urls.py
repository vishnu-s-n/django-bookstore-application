from django.urls import path
from owner import views

urlpatterns=[
    path("index",views.AdminView.as_view(),name="dashboard"),
    path("orders/latest",views.OrdersListView.as_view(),name="neworders"),
    path("order/details<int:id>",views.OrderDetailView.as_view(),name="order-details")

]