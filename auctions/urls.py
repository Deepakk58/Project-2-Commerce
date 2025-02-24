from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/<str:cat_id>", views.displayCategory, name="displayCat"),
    path("watchList", views.displayWatchList, name="watchList"),
    path("<int:listing_id>/add", views.addWatchList, name="addWatchList"),
    path("<int:listing_id>/remove", views.removeWatchList, name="removeWatchList"),
    path("categories", views.category, name="category"),
    path("<int:listing_id>", views.loadListing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.createListing, name="createListing")
]
