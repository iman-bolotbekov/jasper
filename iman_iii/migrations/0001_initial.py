# Generated by Django 4.1.6 on 2023-02-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numbo_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=255)),
                ('second', models.CharField(max_length=255)),
                ('third', models.CharField(max_length=255)),
                ('fourth', models.CharField(max_length=255)),
                ('fifth', models.CharField(max_length=255)),
            ],
        ),
    ]