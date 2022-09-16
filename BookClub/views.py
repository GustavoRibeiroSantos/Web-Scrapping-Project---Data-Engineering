from django.shortcuts import render
from .models import Model

def web_scraper(request):
    web_driver_started = Model.start_selenium()
    Model.getInformation(web_driver_started)