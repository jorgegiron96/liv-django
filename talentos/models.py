from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Talento(models.Model):

    nome = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    etapa = models.CharField(max_length=50)
    video   = models.CharField(max_length=120)
    is_uxdesigner = models.BooleanField(null=True)
    is_uidesigner = models.BooleanField(null=True)
    is_uxwriter = models.BooleanField(null=True)

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
            compet.append('UX Writer')

        compet = ', '.join(compet)

        return compet	
    
    # competencias = models.BooleanField()


class Projeto(models.Model):

    ABOUT_PROJECT_CHOICES = (
    ('0', "Research"),
    ('1', "Wireframe"),
    ('2', "Prototipação"),
    ('3', "Write"),
    ('4', "Strategy"),
    ('5', "Design System"))
    DIAS_SEMANA =(
    ('1', 'Segunda'),
    ('2', 'Terça'),
    ('3', 'Quarta'),
    ('4', 'Quinta'),
    ('5', 'Sexta'))
    HORARIOS = (('1', '8h-12h'),
                ('2', '13h-17h'))

    nome = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    video1  = models.CharField(max_length=120, blank=True, null=True)
    video1_about =   models.CharField(max_length=1, choices=ABOUT_PROJECT_CHOICES, default='0')
    video2  = models.CharField(max_length=120,blank=True, null=True)
    video2_about = models.CharField(max_length=1, choices=ABOUT_PROJECT_CHOICES, default='0')
    video3  = models.CharField(max_length=120,blank=True, null=True)
    video3_about = models.CharField(max_length=1, choices=ABOUT_PROJECT_CHOICES, default='0')
    talento = models.ForeignKey(Talento, on_delete=models.CASCADE)
    horario_entrev = MultiSelectField(choices=HORARIOS,max_choices=5, max_length=30, default='0')
    semana_entrev = MultiSelectField(choices=DIAS_SEMANA,max_choices=5, max_length=30, default='1')

    def __str__(self) -> str:
        return self.nome

#fazer um commit novo.

### chage views

