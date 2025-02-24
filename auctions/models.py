from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.name}"

class Listings(models.Model):
    title = models.CharField(max_length=50)
    descp = models.CharField(max_length=250)
    bid = models.IntegerField()
    url = models.URLField(max_length=200, blank=True)
    category = models.ForeignKey(Category, blank=True, related_name="categorization", on_delete=models.CASCADE, null=True)
    watchList = models.ManyToManyField(User, blank=True, related_name="listingWatchList")
    

    def __str__(str):
        return f"Title: {str.title} Description: {str.descp} Current Bid: {str.bid}"
