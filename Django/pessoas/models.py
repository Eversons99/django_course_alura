from django.db import models

# Create your models here.

# Pessoa representa uma tabela no banco de dados
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)  # Campo da tabela
    email = models.CharField(max_length=200) # Campo da tabela

    def __str__(self):
        return self.nome