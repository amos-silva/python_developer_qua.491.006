from django.db import models # type:ignore

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)  # auto incremento
    nome = models.CharField(max_length=255, null=False, blank=False) # Campo obrigatorio, não vázio
    email = models.EmailField(unique=True, null=False, blank=False)  # Campo unico - não repetido e não vazio
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_nasc = models.DateField(null=False, blank=False)
