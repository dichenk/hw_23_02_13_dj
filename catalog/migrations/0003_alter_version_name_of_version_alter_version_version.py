# Generated by Django 4.1.6 on 2023-02-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_category_alter_version_name_of_version_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='name_of_version',
            field=models.CharField(default=10, max_length=250, verbose_name='Название версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version',
            field=models.CharField(default=10, max_length=250, verbose_name='Номер версии'),
        ),
    ]