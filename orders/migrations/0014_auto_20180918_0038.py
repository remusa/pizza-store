# Generated by Django 2.0.3 on 2018-09-18 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20180906_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/<django.db.models.fields.SlugField>'),
        ),
    ]