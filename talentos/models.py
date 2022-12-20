from django.db import models
from django.contrib.auth.models import User

class Talento(models.Model):

    nome = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    etapa = models.CharField(max_length=50)
    video   = models.CharField(max_length=120)
    is_uxdesigner = models.BooleanField()
    is_uidesigner = models.BooleanField()
    is_uxwriter = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.PROTECT,blank=True,null=True, default=1, related_name='user')
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return self.nome
        
    @property
    def competencias(self):
        compet = []
        if self.is_uxdesigner:
            compet.append('UX Designer')

        if self.is_uidesigner:
            compet.append('UI Designer')

        if self.is_uxwriter:
            compet.append('UX Designer')

        compet = ', '.join(compet)

        return compet	
    
    # competencias = models.BooleanField()


class Projeto(models.Model):

    nome = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    link  = models.CharField(max_length=120)
    talento = models.ForeignKey(Talento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
