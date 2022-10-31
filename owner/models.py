from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    category_name=models.CharField(max_length=150)
    is_active=models.BooleanField(default=True)

    def __str__(self) :
        return self.category_name

class Books(models.Model):
    book_name=models.CharField(max_length=150,unique=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images",null=True)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=150)
    publisher=models.CharField(max_length=150)

class Carts(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="in-cart")
    qty=models.PositiveIntegerField(default=1)

class Orders(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    options=(
        ("order-placed","order-placed"),
        ("dispatched","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="order-placed")
    delivery_address=models.CharField(max_length=200,null=True)
    expected_delivery_date=models.DateTimeField(null=True)