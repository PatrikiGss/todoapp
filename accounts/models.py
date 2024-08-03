from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.core.exceptions import ValidationError # type: ignore

class UserProfile(models.Model):
    photo = models.ImageField('foto', upload_to='photos')
    cell_phone = models.CharField('celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'perfil do usuário'
        verbose_name_plural = 'perfis dos usuários'

    def __str__(self):
        return self.user.username
    
    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.first().id:
            raise ValidationError('Você já tem um perfil cadastrado.')