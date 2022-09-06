from django.db import models
from datetime import datetime

# Create your models here.

# Declarando a minha classe Models
class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)                             # Declarando um campo com uma cadeia de caracteres de tamanho maximo de 200
    ingredientes = models.TextField()                                           # Declarando um campo onde estará contido um texto, sem limites de caracteres
    modo_preparo = models.TextField()                                           # Declarando um campo onde estará contido um texto, sem limites de caracteres
    tempo_preparo = models.IntegerField()                                       # Declarando um campo onde estará contido dados inteiros (Números)
    rendimento = models.CharField(max_length=100)                               # Declarando um campo com uma cadeia de caracteres de tamanho maximo de 100
    categoria = models.CharField(max_length=100)                                # Declarando um campo com uma cadeia de caracteres de tamanho maximo de 100
    data_receita = models.DateTimeField(default = datetime.now, blank = True)   # Declarando um campo com tipo data, valor padrão data atual, caso não pegue a data atual, o campo ficará em branco