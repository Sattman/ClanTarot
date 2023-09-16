from django.contrib import admin

from .models import Produto 


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug','criado', 'modificado', 'ativo')



from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'sexo', 'nascimento','nascionalidade', 'nome_pai', 'nome_mae', 'cor', 'religion')
