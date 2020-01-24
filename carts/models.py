from django.db import models
from users.models import User
from products.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0, max_digits=8, decimal_places=3)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=3)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''
