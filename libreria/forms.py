from django import forms
from .models import Libro,Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model  = Autor
        fields = '__all__'
            

class LibroForm(forms.ModelForm):
    class Meta:
        model  = Libro
        fields = '__all__'
        widgets = {
            'autores_ids': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-group'}),
            'descripcion': forms.Textarea(attrs={'rows': 2, 'cols': 30}),
        }
        
       