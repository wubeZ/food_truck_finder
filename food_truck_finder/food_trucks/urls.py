from django.urls import path
from . import views

app_name = 'food_trucks'

urlpatterns = [
    path("", views.index , name = "index"),
    path("search",views.search, name = "search"),
    path("searchByLoc", views.search_by_location, name = "search_by_location"),
    path("details/<str:id>", views.details, name = "details")  
]