from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=100)
    choices = (
        ("Coat", "Coat"),
        ("Pant", "Pant"),
        ("Inner-Coat", "Inner-Coat"),
        ("Shirt", "Shirt"),
        ("Tie", "Tie"),
        ("Daura-Suruwal", "Daura-Surwal"),
        ("Dhaka-Topi", "Dhaka-Topi"),
        ("Sari", "Sari"),
        ("Kurtha", "Kurtha"),
        ("Lhenga", "Lhenga"),
        ("Ladies-Jeans", "Ladies-Jeans"),
        ("Ladies-Shirt", "Ladies-Shirt"),
        ("Baby-fork", "Baby-fork"),
        ("Baby-pamper", "Baby-pamper"),
    )
    category = models.CharField(max_length=50, choices=choices)
    added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "itemdetail",
            kwargs={"pk": self.pk},
        )


class cart(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name


class bought(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name


class trending(models.Model):
    name = models.CharField(max_length=100)
    added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name