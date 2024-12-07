from django.db import models

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    tipo = models.CharField(max_length=50)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
