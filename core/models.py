from django.db import models
from stdimage.models import StdImageField
from django.utils import timezone
from django.utils.text import slugify
from datetime import date
from django.core.validators import MinValueValidator
# SIGNALS
from django.db.models import signals


class Base(models.Model):
    criado = models.DateField('Data de criação', default=timezone.now)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    estoque = models.IntegerField('Estoque', default=0, validators=[MinValueValidator(0)])
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)

SEX_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
)

COR = (
    ('N', 'Negro'),
    ('B', 'Branco'),
    ('I', 'Índigena'),
    ('A', 'Amarela'),
    ('P', 'Pardo'),
)

class Cliente(models.Model):
    nome_completo = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)    
    sexo = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    nascimento = models.DateField('Data de Nascimento')
    nascionalidade = models.CharField('Nascionalidade', max_length=10, default='Brasileira')
    nome_pai = models.CharField('Nome do Pai', max_length=100)
    nome_mae = models.CharField('Nome da Mãe', max_length=100)
    cor = models.CharField('Cor/Raça', max_length=1, choices=COR, default='Negro')
    religion = models.CharField('Religião', max_length=50)




