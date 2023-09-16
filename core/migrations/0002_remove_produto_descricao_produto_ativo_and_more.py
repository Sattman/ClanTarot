# Generated by Django 4.1.7 on 2023-07-18 19:59

from django.db import migrations, models
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='descricao',
        ),
        migrations.AddField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AddField(
            model_name='produto',
            name='criado',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=0, verbose_name='Estoque'),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=stdimage.models.StdImageField(default=0, force_min_size=False, upload_to='produtos', variations={'thumb': (124, 124)}, verbose_name='Imagem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='modificado',
            field=models.DateField(auto_now=True, verbose_name='Data de atualização'),
        ),
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço'),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]