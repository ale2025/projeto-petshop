from django import forms
from pagina.models import Animal, Petshop

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class PetshopForm(forms.ModelForm)
    class Meta:
        model = Petshop
        fields = '__all__'