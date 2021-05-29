from .models import Car, InspectService
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car


class InspectServiceCreateView(CreateView):
    model = InspectService
    fields = '__all__'
