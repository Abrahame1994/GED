# Generated by Django 4.0.6 on 2022-10-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_traffic_destinataire'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='statut',
            field=models.BooleanField(default=False),
        ),
    ]
