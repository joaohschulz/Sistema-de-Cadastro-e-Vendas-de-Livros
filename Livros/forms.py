from django import forms
from .models import Livro
class InsereLivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'valor',
            'imagem',
        ]