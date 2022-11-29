from tkinter import CASCADE
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import path, include, reverse
from django.conf import settings
from django.contrib import admin

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=200, null=False, blank = False, help_text = 'Nome ccompleto', verbose_name = 'Nome')
    DataNasc = models.DateField(auto_now=False, auto_now_add=False, help_text = 'Data de nascimento no formato aaaa-mm-ss', verbose_name = 'Data de Nascimento')
    # morada = models.CharField(max_lenght=200, null = True, blank = True, help_text = 'Morada completa')
    # codigo_postal = models.CharField(max_length=8, null = True, blank = True)
    # nif = models.CharField(max_length = 9, null = True, blank =True)
    Tel = models.CharField(max_length=12, null = False, help_text = 'Número de de telefone ou telemóvel', verbose_name = 'Nº Telefone')
    email = models.EmailField(max_length = 256, unique=False, blank = True, null=True)
    Notas = models.TextField(blank = True, null=True, verbose_name = 'Notas')
    
    class Meta:
        ordering = ['nome']
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('clientes:clientes-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.nome
    
class Tratamento(models.Model):
    cliente = models.ForeignKey('Clientes', on_delete = models.CASCADE)
    datatrat = models.DateField(auto_now=False, auto_now_add=False, help_text = 'Data em que ocorreu o tratamento', verbose_name = 'Data', default = datetime.date.today)
    escolha = [('Q','TENS'), ('M','Massagem'), ('A','Acupunctura'), ('Q','Quinésio'), ('P','Pistola'), ('O','Outros')]
    tipoTrat = models.CharField(max_length = 1, choices = escolha, default= 'Massagem', help_text = 'Escolha o tipo de tratamento efectuado', verbose_name = 'Tipo de Tratamento')
    Descricao = models.TextField(blank = True, null = True, help_text = 'Descrição do tratamento (Outros), ou observações sobre tratamentos', verbose_name = 'Descrição')
    
    class Meta:
        ordering = ['-datatrat']
   
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.cliente.nome})'
    
class Exames(models.Model):
    cliente = models.ForeignKey('Clientes', on_delete = models.CASCADE)
    dataex = models.DateField(auto_now=False, auto_now_add=False, help_text = 'Data em que foi feito o exame', verbose_name = 'Data')
    Descricao = models.TextField(blank = True, null = True, help_text = 'Descrição e tipo de exame', verbose_name = 'Descrição')
    Ficheiro = models.FileField("", upload_to = settings.EXAMES_ROOT , max_length=100, help_text = 'Escolha o ficheiro com o exame')
    
    class Meta:
        ordering = ['-dataex']
    
    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.cliente.nome)
    
# Modelo para ligação ao calendário do Google com os agendamentos

# Modelo para envio de email/sms de aviso de agendamento