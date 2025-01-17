# Generated by Django 5.0.7 on 2024-07-20 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_author_book_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('bio', models.TextField(max_length=500)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firstapp.author')),
            ],
        ),
    ]
