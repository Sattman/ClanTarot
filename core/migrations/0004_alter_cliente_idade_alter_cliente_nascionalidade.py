# Generated by Django 4.1.7 on 2023-07-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(default=0, verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nascionalidade',
            field=models.CharField(default='Brasileira', max_length=10, verbose_name='Nascionalidade'),
        ),
    ]
