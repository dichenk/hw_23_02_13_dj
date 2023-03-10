# Generated by Django 4.1.6 on 2023-02-23 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Наименование')),
                ('info', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=250, verbose_name='Наименование')),
                ('info', models.TextField(null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение (превью)')),
                ('price', models.CharField(max_length=250, null=True, verbose_name='Цена за покупку')),
                ('date_create', models.DateField(auto_now_add=True, null=True, verbose_name='Created Time')),
                ('date_last_change', models.DateField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_of_the_current_version', models.CharField(auto_created=True, choices=[('current version', 'текущая версия'), ('previous version', 'предыдущая версия')], default='current version', max_length=22)),
                ('version', models.CharField(default=10, max_length=250, verbose_name='Номер версии')),
                ('name_of_version', models.CharField(default=10, max_length=250, verbose_name='Название версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
