# Generated by Django 3.2.4 on 2021-07-15 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210130_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
