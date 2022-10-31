from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,FormView,DetailView,ListView
from customer import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Books,Categories,Carts,Orders


# Create your views here.
class RegistrationView(CreateView):
    form_class=forms.RegistrationForm
    template_name="registration.html"
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request,"Your account has been created")
        return super().form_valid(form)

class LoginView(FormView):
    template_name="login.html"
    form_class=forms.LoginForm

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST,files=request.FILES)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)

            if user:
                login(request,user)

                if request.user.is_superuser:
                    return redirect("dashboard")
                else:

                    return redirect("home")
                
                
            else:
                messages.error(request,"Invalid username or password")
                return render(request,"login.html",{"form":form})

class HomeView(TemplateView):
    template_name="home.html"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_books=Books.objects.all()
        context["books"]=all_books
        return context

class BookDetailView(DetailView):
    template_name="book-detail.html"
    model=Books
    context_object_name="book"
    pk_url_kwarg="id"

class AddtoCart(FormView):
    template_name="addto-cart.html"
    form_class=forms.CartForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.CartForm(),"book":book})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(book=book,user=user,qty=qty)
        messages.success(request,"Added to cart")
        return redirect("home")

class MyCartView(ListView):
    model=Carts
    template_name="cart-list.html"
    context_object_name="carts"

    def get_queryset(self) :
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")



def cart_item_remove(request,*args,**kwargs):
    
    cart_id=kwargs.get("id")
    cart=Carts.objects.get(id=cart_id)
    cart.status="cancelled"
    cart.save()
    messages.success(request,"Item Removed")
    return redirect("mycart")

class PlaceOrderView(FormView):
    template_name="place-order.html"
    form_class=forms.OrderForm
    context_object_name="orders"

    # def get_queryset(self) :
    #     return Orders.objects.filter(user=self.request.user).order_by("delivery_date")


    def post(self,request,*args,**kwargs):
        cart_id=kwargs.get("cid")
        book_id=kwargs.get("pid")
        cart=Carts.objects.get(id=cart_id)
        book=Books.objects.get(id=book_id)
        user=request.user
        delivery_address=request.POST.get("delivery_address")
        Orders.objects.create(book=book,user=user,delivery_address=delivery_address)
        cart.status="order-placed"
        cart.save()
        messages.success(request,"Added to cart")
        return redirect("home")

    

    

