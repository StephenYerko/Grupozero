# Generated by Django 4.2.1 on 2023-07-13 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appGrupoZero', '0013_alter_obra_artista'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='obra',
            name='artista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appGrupoZero.artista'),
        ),
    ]
