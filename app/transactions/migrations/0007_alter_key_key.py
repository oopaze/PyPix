# Generated by Django 3.2.9 on 2021-11-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_alter_key_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='key',
            field=models.CharField(max_length=100, unique=True, verbose_name='Chave'),
        ),
    ]
