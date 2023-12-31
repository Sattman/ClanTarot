# Generated by Django 4.1.7 on 2023-07-22 21:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_cliente_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
    ]
