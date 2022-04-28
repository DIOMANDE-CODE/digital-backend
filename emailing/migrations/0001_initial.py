# Generated by Django 4.0.4 on 2022-04-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name="Nom de l'utilisateur")),
                ('mail', models.EmailField(max_length=100, verbose_name='Adresse email')),
                ('sujet', models.CharField(max_length=100, verbose_name='Sujet du mail')),
                ('message', models.TextField()),
            ],
        ),
    ]
