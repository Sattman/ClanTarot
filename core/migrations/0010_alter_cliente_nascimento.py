# Generated by Django 4.1.7 on 2023-07-22 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_cliente_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nascimento',
            field=models.DateField(auto_now=True, verbose_name='Data de Nascimento'),
        ),
    ]