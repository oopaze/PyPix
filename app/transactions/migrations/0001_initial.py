# Generated by Django 3.2.9 on 2021-11-12 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('RA', 'Aleatória'), ('PH', 'Telefone')], default='RA', max_length=10, verbose_name='Tipo')),
                ('key', models.CharField(max_length=100, verbose_name='Chave')),
            ],
        ),
        migrations.CreateModel(
            name='Transction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor')),
                ('send_at', models.DateField(auto_now_add=True, verbose_name='Enviado em')),
                ('receiver_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='transactions.key')),
                ('sender_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='transactions.key')),
            ],
        ),
    ]
