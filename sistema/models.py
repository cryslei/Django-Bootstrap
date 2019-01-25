from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    class Meta:
        verbose_name = 'Cadastrar Categoria'
        verbose_name_plural = 'Cadastrar Categorias'
    nome = models.CharField(max_length=64)
    def __str__(self):
        return self.nome

class Estado(models.Model):
    class Meta:
        verbose_name = 'Cadastrar Estado'
        verbose_name_plural = 'Cadastrar Estados'
    nome = models.CharField(max_length=64)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome

class Setor(models.Model):
    class Meta:
        verbose_name = 'Cadastrar Setor'
        verbose_name_plural = 'Cadastrar Setores'
    nome = models.CharField(max_length=64)

    def __str__(self):
        return self.nome

class Relatorio(models.Model):
    class Meta:
        verbose_name = 'Relatorio'
        verbose_name_plural = 'Relatorios'
	
    patrimonio = models.CharField(max_length=4)
    tecnico = models.CharField(max_length=128,blank = True,null = True)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    nome = models.CharField('nome do equipamento',max_length=128)
    serie = models.CharField(max_length=64)
    marca = models.CharField(max_length=32)
    setor = models.ForeignKey(Setor,on_delete=models.CASCADE)
    data_saida = models.DateField('Data de saída',blank = True,null = True)
    data_retorno = models.DateField('Data de retorno',blank = True,null = True)
    descricao = models.TextField('Descrição',blank=True, null=True)

    