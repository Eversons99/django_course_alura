from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

# Create your models here.

# Declarando a minha classe Models
class Receita(models.Model):
    pessoas = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)                             # Declarando um campo com uma cadeia de caracteres de tamanho maximo de 200
    ingredientes = models.TextField()                                           # Declarando um campo onde estará contido um texto, sem limites de caracteres
    modo_preparo = models.TextField()                                           # Declarando um campo onde estará contido um texto, sem limites de caracteres
    tempo_preparo = models.IntegerField()                                       # Declarando um campo onde estará contido dados inteiros (Números)
    rendimento = models.CharField(max_length=100)                               # Declarando um campo com uma cadeia de caracteres de tamanho maximo de 100
    categoria = models.CharField(max_length=100)                                # Declarando um campo com uma cadeia de caracteres de tamanho maximo de 100
    data_receita = models.DateTimeField(default=datetime.now, blank = True)     # Declarando um campo com tipo data, valor padrão data atual, caso não pegue a data atual, o campo ficará em branco
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)   # Declarando um campo com tipo image, a imagem estara no caminho informado no upload e o segundo parametro é para caso uma imagem não exista
    publicada = models.BooleanField(default=False)                              # Declarando um campo com uma boolean, valor padrão False
    def __str__(self):
        return self.nome_receita