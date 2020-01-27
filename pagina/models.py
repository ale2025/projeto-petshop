from django.db import models

# Create your models here.
class Petshop(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.CharField(max_length=9)
    email = models.EmailField()
    cep = models.CharField(max_length=9)
    numero = models.IntegerField()
    generos = ( 
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )
    genero = models.CharField(max_length=3,choices=generos)
    celular = models.CharField(max_length=13)
    motivo = models.TextField(max_length=255)

class Animal(models.Model):
    animal = models.CharField(max_length=255)
    nome_pet = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    portes = (
        ('P','Pequeno'),
        ('M','Medio'),
        ('G','Grande'),
    )
    porte = models.CharField(max_length=3,choices=portes)
    peso = models.IntegerField()