import datetime
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .managers import *


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email", max_length=255)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            username_base = self.email.split("@")[0]
            username = username_base
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{username_base}{counter}"
                counter += 1
            self.username = username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider/images")
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/images", default=None)
    name = models.CharField(max_length=15)
    position = models.CharField(max_length=15)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Quote(models.Model):
    name = models.CharField(max_length=15)
    emial = models.CharField(max_length=15)
    service = models.TextField(max_length=100)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class PrintingServices(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to="printingservice/images")

    def __str__(self):
        return self.title


class ItServices(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to="itservice/images")
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class PhotographyServices(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to="photographyservice/images")
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class GetItServices(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=100)
    comment = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class GetPhotographyServices(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10)
    comment = models.TextField(max_length=200)

    def __str__(self):
        return self.name
