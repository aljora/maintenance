from .models import Inspection, InspectService
from django.forms import ModelForm


class InspectServiceForm(ModelForm):
    class Meta:
        model = InspectService
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        get = False
        if 'car' in kwargs:
            car = kwargs.pop('car')
            get = True
        super().__init__(*args, **kwargs)
        if get:
            options = Inspection.objects.filter(part__car__pk=car)
            self.fields['activity'].queryset = options
