# Generated by Django 4.1.4 on 2022-12-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatBreeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('origin', models.CharField(max_length=255, verbose_name='Origem')),
                ('temperament', models.CharField(max_length=255, verbose_name='Temperamento')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('date_modified', models.DateTimeField(auto_now_add=True, verbose_name='Data Modificação')),
            ],
            options={
                'verbose_name': 'Cat Breed',
                'verbose_name_plural': 'Cats Breeds',
                'db_table': 'cat_breeds',
                'ordering': ['id'],
                'managed': True,
            },
        ),
    ]
