from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
            'description',
            'category',
            'location',
            'salary',
            'duration_days',
            'number_of_workers',
            'latitude',
            'longitude',
            
        ]
        widgets = {
            'latitude': forms.TextInput(attrs={'id': 'latitude-field'}),
            'longitude': forms.TextInput(attrs={ 'id': 'longitude-field'}),
        }


