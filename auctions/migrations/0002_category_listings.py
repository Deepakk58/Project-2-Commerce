# Generated by Django 5.1.5 on 2025-02-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descp', models.CharField(max_length=250)),
                ('startBid', models.IntegerField()),
                ('url', models.URLField(blank=True)),
                ('category', models.ManyToManyField(blank=True, related_name='categorization', to='auctions.category')),
            ],
        ),
    ]
