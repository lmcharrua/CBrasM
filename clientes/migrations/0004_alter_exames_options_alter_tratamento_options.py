# Generated by Django 4.1.1 on 2022-10-03 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_clientes_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exames',
            options={'ordering': ['-data']},
        ),
        migrations.AlterModelOptions(
            name='tratamento',
            options={'ordering': ['-data']},
        ),
    ]
