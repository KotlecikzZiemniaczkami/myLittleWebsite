from django.urls import path
from . import views

urlpatterns = [
    path("locations/", views.index),
    path("<location>/", views.loc)
]