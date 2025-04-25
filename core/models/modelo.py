from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, null=True, blank=True)
    categoria = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        if self.marca:
            return f'{self.id} {self.nome.upper()} {self.marca.upper()}'
        else:
            return f'{self.id} {self.nome.upper()}'