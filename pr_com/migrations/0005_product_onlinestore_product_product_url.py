# Generated by Django 4.1.7 on 2023-07-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr_com', '0004_remove_product_feature_bullets_remove_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='onlineStore',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_url',
            field=models.URLField(blank=True),
        ),
    ]
