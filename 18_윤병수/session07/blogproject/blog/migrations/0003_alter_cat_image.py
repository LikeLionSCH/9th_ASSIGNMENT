# Generated by Django 3.2.4 on 2021-06-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cat/'),
        ),
    ]
