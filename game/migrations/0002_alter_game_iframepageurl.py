# Generated by Django 4.2.9 on 2025-01-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='iframePageUrl',
            field=models.CharField(max_length=50, verbose_name='Play_Html'),
        ),
    ]
