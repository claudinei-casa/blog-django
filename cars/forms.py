from django import forms

from .models import Cars


class CreateCar(forms.ModelForm):
    class Meta:
        model = Cars
        # fields = ('brand', 'description', 'price', 'color', 'opt',)
        fields = '__all__'
