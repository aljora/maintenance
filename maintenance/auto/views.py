from .models import InspectService
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


def index(request):
    return render(request, 'auto/index.html')


class InspectServiceCreateView(CreateView):
    model = InspectService
    fields = '__all__'
