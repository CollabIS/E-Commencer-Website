# Generated by Django 4.2.7 on 2024-01-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommencer', '0004_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]