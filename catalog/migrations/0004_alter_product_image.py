# Generated by Django 4.1.6 on 2023-02-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение (превью)'),
        ),
    ]