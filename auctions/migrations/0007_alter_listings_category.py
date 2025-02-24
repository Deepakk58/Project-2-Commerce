# Generated by Django 5.1.5 on 2025-02-24 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorization', to='auctions.category'),
        ),
    ]
