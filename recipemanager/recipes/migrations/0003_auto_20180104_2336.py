# Generated by Django 2.0.1 on 2018-01-04 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20180104_2335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'permissions': (('view_recipe', 'Can view recipe'),)},
        ),
    ]
