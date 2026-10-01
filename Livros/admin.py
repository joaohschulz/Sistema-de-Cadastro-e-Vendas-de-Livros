from django.contrib import admin
from Livros.models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'valor', 'imagem']
admin.site.register(Livro, LivroAdmin)



    
