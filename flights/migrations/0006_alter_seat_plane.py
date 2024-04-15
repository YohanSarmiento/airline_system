# Generated by Django 5.0.4 on 2024-04-13 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_seat_seat_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='plane',
            field=models.ForeignKey(help_text='Avión al que pertenece el asiento', on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='flights.plane'),
        ),
    ]
