from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.title


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
