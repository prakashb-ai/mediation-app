# Generated by Django 5.0 on 2023-12-23 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediation_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediaitonprofile',
            old_name='uername',
            new_name='username',
        ),
    ]
