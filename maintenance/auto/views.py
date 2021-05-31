from .forms import InspectServiceForm
from .models import Car, Inspection, InspectService
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
    form_class = InspectServiceForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['car'] = self.kwargs['car']
        return kwargs


class InspectionCreateView(CreateView):
    model = Inspection
    exclude = ['duration']
