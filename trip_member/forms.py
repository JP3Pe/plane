from django.forms import ModelForm

from trip_member.models import TripMember


class TripMemberForm(ModelForm):
    class Meta:
        model = TripMember
        fields = ['trip']
        labels = {
            'trip': 'trip'
        }
