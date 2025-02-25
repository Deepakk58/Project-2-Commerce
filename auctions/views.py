from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def addBid(request, listing_id):
    if request.method == "POST":
        listing = Listings.objects.get(pk = listing_id)
        bid = float(request.POST["bid"])

        isadded = request.user in listing.watchList.all()
        comments = Comment.objects.filter(post=listing)        
        if listing.price.bid >= bid:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "isadded": isadded,
                "comments": comments,
                "Bmessage": "Bid must be greater than current bid"
            })
        else:
            newBid = Bid(bid = bid, bidder = request.user)
            newBid.save()
            listing.price = newBid
            listing.save()

            return render(request, "auctions/listing.html", {
                "listing": listing,
                "isadded": isadded,
                "comments": comments,
                "Bmessage": "Bid Added Succesfully"
            })

def closeAuction(request, listing_id):
    listing = Listings.objects.get(pk = listing_id)
    listing.isActive = False
    listing.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,))) 

def addComment(request, listing_id):
    if request.method == "POST":
        listing = Listings.objects.get(pk = listing_id)
        msg = request.POST['comment']
        writer = request.user
        comment = Comment(
            post = listing,
            writer = writer,
            message = msg
        )
        comment.save()

        return HttpResponseRedirect(reverse("listing", args=(listing_id,))) 

def displayWatchList(request):
    currUser = request.user
    listings = currUser.listingWatchList.all()
    return render(request, "auctions/index.html", {
        "listings": listings,
        "title": "Watchlist"
    })

def removeWatchList(request, listing_id):
    currUser = request.user
    listing = Listings.objects.get(pk = listing_id)
    listing.watchList.remove(currUser)
    return HttpResponseRedirect(reverse("watchList"))

def addWatchList(request, listing_id):
    currUser = request.user
    listing = Listings.objects.get(pk = listing_id)
    listing.watchList.add(currUser)
    return HttpResponseRedirect(reverse("watchList"))

def displayCategory(request, cat_id):
    cat = Category.objects.get(pk = cat_id)
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.filter(category = cat),
        "title": f"{cat.name}"
    })

def category(request):
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })

def loadListing(request, listing_id):
    currUser = request.user
    listing = Listings.objects.filter(pk=listing_id).first()
    isadded = currUser in listing.watchList.all()
    comments = Comment.objects.filter(post=listing)


    return render(request, "auctions/listing.html", {
        "listing": listing,
        "isadded": isadded,
        "comments": comments
    })

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all(),
        "title": "Active Listings"
    })

def createListing(request):
    if request.method == "POST":
        title = request.POST["title"]
        descp = request.POST["descp"]
        start = request.POST["start"]
        url = request.POST["url"]
        currUser = request.user
        bid = Bid(bid = start, bidder = currUser)
        bid.save()
        cate_id = (request.POST.get("category"))
        if cate_id == "":
            cate = None
        else:
            cate = Category.objects.filter(pk=int(cate_id)).first()

        newList = Listings(
            title = title,
            descp = descp,
            price = bid,
            url = url,
            category = cate,
            owner = currUser
        )

        newList.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        "categories": Category.objects.all()
    })




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
