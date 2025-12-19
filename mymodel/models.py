from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
