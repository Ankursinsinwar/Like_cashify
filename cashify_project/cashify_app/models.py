from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]

    device_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    accessories = models.CharField(max_length=100)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    # image = models.ImageField(upload_to='device_images/', null=True, blank=True)
    image = models.FileField(upload_to='device_images')

    def __str__(self):
        return self.device_name

class DeviceList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.device.device_name}"


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
