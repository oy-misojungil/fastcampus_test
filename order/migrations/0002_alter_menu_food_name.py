# Generated by Django 4.1.4 on 2023-01-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='food_name',
            field=models.CharField(max_length=25),
        ),
    ]
