# Generated by Django 3.0.7 on 2020-06-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutMe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(upload_to='AboutMe/images'),
        ),
    ]
