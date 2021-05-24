from django.contrib import admin
from .models import FuelService
from .models import PartService, Inspection, Replacement, PartType, Part
from .models import Make, CarModel, Car

# Register your models here.
admin.site.register(FuelService)
admin.site.register(PartService)
admin.site.register(Inspection)
admin.site.register(Replacement)
admin.site.register(PartType)
admin.site.register(Part)
admin.site.register(Make)
admin.site.register(CarModel)
admin.site.register(Car)
