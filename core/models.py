from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any custom fields here if needed
    pass

class Coupon(models.Model):
    coupon_id = models.CharField(max_length=10, primary_key=True)
    coupon_code = models.CharField(max_length=32, unique=True)
    expiry_date = models.DateField()
    discount_percentage = models.FloatField()
    max_usage = models.IntegerField(default=2)

    def __str__(self):
        return self.coupon_code


class Franchise(models.Model):
    franchise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MarketingTeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.FloatField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating})"

class AppUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

# class Admin(models.Model):
#     name = models.CharField(max_length=100)  # example field
#     # Add other fields as needed


class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
