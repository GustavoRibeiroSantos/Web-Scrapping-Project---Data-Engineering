from django.urls import path
from .views import web_scraper

urlpatterns = [
    path('',web_scraper),
]