from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.name}"

    
class Bid(models.Model):
    bid = models.IntegerField()
    bidder = models.ForeignKey(User, related_name="bidder", on_delete=models.CASCADE)

    def __str__(self):
        return f"Current Bid: {self.bid} by {self.bidder}"


class Listings(models.Model):
    title = models.CharField(max_length=50)
    descp = models.CharField(max_length=250)
    price = models.ForeignKey(Bid, related_name="price", on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True)
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, related_name="categorization", on_delete=models.CASCADE, null=True)
    watchList = models.ManyToManyField(User, blank=True, related_name="listingWatchList")
    
    def __str__(self):
        return f"Title: {self.title} Description: {self.descp} {self.price}"


class Comment(models.Model):
    message = models.CharField(max_length=200)
    writer = models.ForeignKey(User, related_name="user", blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Listings, related_name="post", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message}: {self.writer}"