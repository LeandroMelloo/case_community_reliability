# Generated by Django 4.1.4 on 2022-12-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catbreeds',
            name='id_breeds',
            field=models.CharField(default=1, max_length=255, verbose_name='Id Breeds'),
            preserve_default=False,
        ),
    ]