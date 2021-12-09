from django.forms import ModelForm, Textarea, TextInput, DateField

from trip.models import Trip


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'content', 'date', 'author']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'minlength': 1, 'maxlength': 50,
                                      'placeholder': '50자 이내로 제목 입력 가능합니다.'}),
            'content': Textarea(attrs={'class': 'form-control'}),
            'date': DateField(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'title',
            'content': 'content',
            'date': 'date',
            'author': 'author'
        }
