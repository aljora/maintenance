from .forms import InspectionForm, InspectServiceForm
from .forms import ReplacementForm, ReplaceServiceForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inspectionform'] = InspectionForm()
        context['replacementform'] = ReplacementForm()
        return context


class InspectionDetailView(DetailView):
    model = Inspection
    template_name = 'auto/activity_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InspectServiceForm()
        return context


class ReplacementDetailView(DetailView):
    model = Replacement
    template_name = 'auto/activity_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplaceServiceForm()
        return context


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
    form_class = InspectionForm


class ReplacementCreateView(CreateView):
    model = Replacement
    form_class = ReplacementForm
