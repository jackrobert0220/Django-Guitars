from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(View):
    template_name = "about.html"

class GuitarList(TemplateView):
    template_name = 'guitarlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guitars"] = guitars
        return context

class Guitar:
    def __init__(self, brand, model, year, price, string_count, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.string_count = string_count
        self.color = color

guitars = [
    Guitar("Fender", "Telecaster", 1958, 1776.09, 6, "white"),
]