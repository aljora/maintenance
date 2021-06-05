import datetime
from .models import Inspection, InspectService, Replacement, DAYSPERMONTH
from django.core.exceptions import ValidationError
from django.forms import DurationField
from django.forms import ModelForm


class MonthField(DurationField):
    def to_python(self, value):
        print('HERE')
        if value in self.empty_values:
            return None
        if isinstance(value, datetime.timedelta):
            return value
        try:
            value = datetime.timedelta(days=int(value)*DAYSPERMONTH)
        except OverflowError:
            raise ValidationError(self.error_messages['overflow'].format(
                min_days=datetime.timedelta.min.days,
                max_days=datetime.timedelta.max.days,
            ), code='overflow')
        if value is None:
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value


class InspectionForm(ModelForm):
    duration = MonthField()


    class Meta:
        model = Inspection
        fields = '__all__'


class ReplacementForm(ModelForm):
    class Meta:
        model = Replacement
        fields = '__all__'
        exclude = ['duration']


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
