from django import forms

from .models import Cars


class CreateCar(forms.ModelForm):

    class Meta:
        model = Cars
        fields = ('__all__')
        prepopulated_fields = {"slug": ("title",)}
