# Generated by Django 4.1.6 on 2023-02-23 21:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='info',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Описание'),
        ),
    ]
