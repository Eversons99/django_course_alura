from django.contrib import admin
from .models import Receita

# Register your models here.

# Criando um novo classe que ir autilizar um método já exitente (list_display) para rendeirzar o id e o nome da receita no Django Admin
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
    # Definindo id e nome da receita como link
    list_display_links = ('id', 'nome_receita')
    # quando alguem digitar o nome de uma receita ela será buscada
    search_fields = ('nome_receita',)
    # Aplicando um filtro por categoria
    list_filter = ('categoria',)
    # Criando uma paginação, neste caso eu escolho o número de items que eu quero por página
    list_per_page = 2

admin.site.register(Receita, ListandoReceitas)

