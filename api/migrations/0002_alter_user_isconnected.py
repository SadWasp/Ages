# Generated by Django 3.2.5 on 2021-09-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isConnected',
            field=models.TextField(),
        ),
    ]