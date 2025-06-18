from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100, default="general")
    price = models.FloatField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to="products/", default="products/default.png")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # use string here
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.title} ({self.user.username})"
