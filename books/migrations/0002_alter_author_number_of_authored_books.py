# Generated by Django 4.2 on 2025-01-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='number_of_authored_books',
            field=models.SmallIntegerField(),
        ),
    ]
