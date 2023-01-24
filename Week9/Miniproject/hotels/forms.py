from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['hotel', 'avis', 'reservation', 'sortit', 'user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hotel'].widget.attrs.update({'class': 'custom-select'})
        self.fields['reservation'].widget.attrs.update({'type':'date'})
        self.fields['sortit'].widget.attrs.update({'type':'date'})
        self.fields['avis'].widget.attrs.update({'class':'form-control'})