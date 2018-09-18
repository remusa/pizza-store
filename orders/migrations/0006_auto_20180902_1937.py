# Generated by Django 2.0.3 on 2018-09-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20180902_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='type',
            field=models.CharField(choices=[('pizza_sicilian', 'Sicilian Pizza'), ('salads', 'Salads'), ('pizza_regular', 'Regular Pizza'), ('pasta', 'Pasta'), ('subs', 'Subs'), ('toppings', 'Toppings'), ('dinner_platters', 'Dinner Platters')], max_length=30),
        ),
    ]
