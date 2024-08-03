from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore

# Create your models here.

class Category(models.Model):
    name = models.CharField('nome', max_length=150)
    description = models.TextField('descrição', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']

    def __str__(self):
        return self.name
        
class Task(models.Model):
    PRIORITY_CHOICES = (
        ('B', 'Baixa🟢'),
        ('M', 'Media🟡'),
        ('A', 'Alta🔴'),
    )
    STATUS_CHOICES = (
        ('EX', 'Em execução🏗️'),
        ('PD', 'Pendente⏳'),
        ('CD', 'Concluida✅'),
    )
    name = models.CharField('tarefa', max_length=200)
    description = models.TextField('descrição')
    end_date = models.DateField('data final', auto_now=False, auto_now_add=False)
    priority = models.CharField('prioridade', max_length=1, choices=PRIORITY_CHOICES)
    category = models.ManyToManyField(Category)
    status = models.CharField('status', max_length=50, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'
        ordering = ['id']
    
    def __str__(self):
        return self.name
