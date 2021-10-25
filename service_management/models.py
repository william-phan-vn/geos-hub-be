from django.db import models
from django.core.validators import MinValueValidator


class OsPlatform(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ServicePrice(models.Model):
    service_code = models.CharField(max_length=10)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    os_platform = models.ForeignKey(OsPlatform, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])  # in USD
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_code
