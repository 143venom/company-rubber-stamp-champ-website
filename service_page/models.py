from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(default="defaultpost.jpg", upload_to="images/services")

    def __str__(self):
        return self.title
