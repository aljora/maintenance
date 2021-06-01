from .forms import InspectServiceForm
from .models import Car, Inspection, InspectService, Part, Replacement
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car


class PartDetailView(DetailView):
    model = Part


class InspectionDetailView(DetailView):
    model = Inspection
    template_name = 'auto/activity_detail.html'


class ReplacementDetailView(DetailView):
    model = Replacement
    template_name = 'auto/activity_detail.html'


class InspectServiceCreateView(CreateView):
    model = InspectService
    form_class = InspectServiceForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'car' in self.kwargs:
            kwargs['car'] = self.kwargs['car']
        return kwargs


class InspectionCreateView(CreateView):
    model = Inspection
    fields = '__all__'
    exclude = ['duration']
