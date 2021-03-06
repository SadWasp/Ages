# Generated by Django 3.2.5 on 2021-09-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('location', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'ordering': ['quantity'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.TextField()),
                ('password', models.TextField()),
                ('role', models.TextField()),
                ('nbOrdersFilled', models.IntegerField()),
                ('isConnected', models.BooleanField()),
            ],
            options={
                'ordering': ['role'],
            },
        ),
    ]
