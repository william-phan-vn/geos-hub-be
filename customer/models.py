from django.db import models

from services.models import ServicePrice


class Customer(models.Model):
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class PaidCustomer(models.Model):
    description = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(ServicePrice, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
