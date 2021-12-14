from django.forms import ModelForm, Textarea, TextInput

from trip.models import Trip


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'explanation']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'minlength': 1, 'maxlength': 50,
                                      'placeholder': '50자 이내로 제목 입력 가능합니다.'}),
            'explanation': Textarea(attrs={'class': 'form-control', 'row': 3}),
        }
        labels = {
            'title': 'title',
            'explanation': 'explanation',
        }
