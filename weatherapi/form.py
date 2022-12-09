from django.forms import ModelForm, TextInput
from .models import City

class CityFormRequest(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(
            attrs={ 'class': 'form-control', 
                    'placeholder': 'City Name'
                    }
                    )
                    }