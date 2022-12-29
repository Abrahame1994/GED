# Generated by Django 4.0.6 on 2022-10-11 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_courrier_statut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='premier', to='App.apparts')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second', to='App.apparts')),
            ],
        ),
    ]