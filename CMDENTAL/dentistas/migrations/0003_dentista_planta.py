# Generated by Django 4.2 on 2024-07-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentistas', '0002_remove_dentista_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentista',
            name='planta',
            field=models.BooleanField(default=False),
        ),
    ]
