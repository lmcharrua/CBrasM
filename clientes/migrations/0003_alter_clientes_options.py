# Generated by Django 4.1.1 on 2022-10-03 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_clientes_datanasc_alter_clientes_notas_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ['nome']},
        ),
    ]