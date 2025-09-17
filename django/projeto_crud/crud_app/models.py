from django.db import models # type:ignore

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)  # auto incremento
    nome = models.CharField(max_length=255, null=False, blank=False) # Campo obrigatorio, não vázio
    email = models.EmailField(unique=True, null=False, blank=False)  # Campo unico - não repetido e não vazio
    cpf = models.CharField(max_length=14,unique=True,null=True, blank=True)

    # server para mostrar o nome correto na pagina de admin, ao invéz de mostrar o nome da classe
    def __str__(self):
        return self.nome
