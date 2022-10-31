from django.shortcuts import render,redirect

from django.views.generic import TemplateView,ListView,DetailView
from owner.models import Orders
from owner.forms import OrderUpdateForm
from django.core.mail import send_mail
# Create your views here.

class AdminView(TemplateView):
    template_name="dashboard.html"
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        cnt=Orders.objects.filter(status="order-placed").count()
        context["count"]=cnt
        return context

class OrdersListView(ListView):
    model=Orders
    context_object_name="orders"
    template_name="admin-list.html"
    
    def get_queryset(self):
        return Orders.objects.filter(status="order-placed")

class OrderDetailView(DetailView):
    model=Orders
    template_name="order-detail.html"
    pk_url_kwarg="id"
    context_object_name="order"

    def get_context_data(self, **kwargs): 
        context=super().get_context_data()
        form=OrderUpdateForm()
        context["form"]=form
        return context

    def post(self,request,*args,**kwargs):
        order=self.get_object()
        form=OrderUpdateForm(request.POST)
        if form.is_valid():
            order.status=form.cleaned_data.get("status")
            order.expected_delivery_date=form.cleaned_data.get("expected_delivery_date")
            dt=form.cleaned_data.get("expected_delivery_date")
            order.save()
            send_mail(
                "Order delivery update Bookmark",
                f"Your order will be delivered on{dt}",
                "vishnusnair305@gmail.com",
                ["techievs16@gmail.com"]
            )
            return redirect("dashboard")