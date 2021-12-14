from django.forms import ModelForm, TextInput

from schedule.models import Schedule


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['place']
        widgets = {
            'place': TextInput(
                attrs={'class': 'form-control'})
        }
        labels = {
            'place': 'place'
        }
