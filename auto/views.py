from .forms import InspectionForm, InspectServiceForm
from .forms import ReplacementForm, ReplaceServiceForm
from .forms import FuelServiceForm
from .forms import PartForm
from .models import Car, Inspection, InspectService, Part
from .models import Replacement, ReplaceService
from .models import FuelService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PartForm()
        return context


class PartDetailView(DetailView):
    model = Part

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inspectionform'] = InspectionForm()
        context['replacementform'] = ReplacementForm()
        return context


class InspectionDetailView(DetailView):
    model = Inspection
    template_name = 'auto/inspection_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InspectServiceForm()
        return context


class ReplacementDetailView(DetailView):
    model = Replacement
    template_name = 'auto/replacement_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplaceServiceForm()
        return context


class FuelDetailView(DetailView):
    model = Car
    template_name = 'auto/fuel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FuelServiceForm()
        return context


class InspectServiceCreateView(LoginRequiredMixin, CreateView):
    model = InspectService
    form_class = InspectServiceForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'car' in self.kwargs:
            kwargs['car'] = self.kwargs['car']
        return kwargs


class ReplaceServiceCreateView(LoginRequiredMixin, CreateView):
    model = ReplaceService
    form_class = ReplaceServiceForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'car' in self.kwargs:
            kwargs['car'] = self.kwargs['car']
        return kwargs


class FuelServiceCreateView(LoginRequiredMixin, CreateView):
    model = FuelService
    form_class = FuelServiceForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'car' in self.kwargs:
            kwargs['car'] = self.kwargs['car']
        return kwargs


class PartCreateView(LoginRequiredMixin, CreateView):
    model = Part
    form_class = PartForm


class InspectionCreateView(LoginRequiredMixin, CreateView):
    model = Inspection
    form_class = InspectionForm


class ReplacementCreateView(LoginRequiredMixin, CreateView):
    model = Replacement
    form_class = ReplacementForm
