# Generated by Django 4.2.7 on 2024-01-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommencer', '0003_remove_customer_email_remove_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('WHITE', 'White'), ('BLACK', 'Black'), ('MULTICOLOR', 'Multicolor'), ('RED', 'Red'), ('BROWN', 'Brown'), ('BLUE', 'Blue')], default='WHITE', max_length=10),
        ),
    ]
