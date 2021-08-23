from django.contrib import admin
from .models import FuelService
from .models import InspectService, Inspection
from .models import ReplaceService, Replacement
from .models import PartType, Part
from .models import Make, CarModel, Car

# Register your models here.
admin.site.register(FuelService)
admin.site.register(InspectService)
admin.site.register(Inspection)
admin.site.register(ReplaceService)
admin.site.register(Replacement)
admin.site.register(PartType)
admin.site.register(Part)
admin.site.register(Make)
admin.site.register(CarModel)
admin.site.register(Car)
