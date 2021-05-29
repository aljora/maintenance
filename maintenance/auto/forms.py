from .models import Inspection, InspectService
from django.forms import ModelForm


class InspectServiceForm(ModelForm):
    class Meta:
       model = InspectService
       fields = '__all__'

    def __init__(self, *args, **kwargs):
        print(args)
        car = kwargs.pop('car')
        super().__init__(*args, **kwargs)
        self.fields['activity'].queryset = Inspection.objects.filter(part__car__pk=car)
