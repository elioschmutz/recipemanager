# Generated by Django 2.0.1 on 2018-01-07 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180107_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='duration',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='portions',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='www',
            field=models.URLField(blank=True),
        ),
    ]