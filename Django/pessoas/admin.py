from django.contrib import admin
from .models import Pessoa
# Register your models here.

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    # Definindo id e nome da receita como link
    list_display_links = ('id', 'nome')
    # quando alguem digitar o nome de uma receita ela será buscada
    search_fields = ('nome',)
    # Criando uma paginação, neste caso eu escolho o número de items que eu quero por página
    list_per_page = 2

admin.site.register(Pessoa, ListandoPessoas)

