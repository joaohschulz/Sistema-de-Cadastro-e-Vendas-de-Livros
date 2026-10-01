from django.db import models


class CategoriaLivro(models.Model):
    nome = models.CharField(max_length=30, null=False)
    def __str__(self):
        return f"Categoria: {self.nome}"


class DisponibilidadeLivro(models.Model):
    disponivel = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f"Disponibilidade: {self.disponivel}"


class Livro(models.Model):
    titulo = models.CharField(max_length=40, null=False)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    imagem = models.ImageField(upload_to='capas/')
    def __str__(self):
        return f"Título: {self.titulo}"
