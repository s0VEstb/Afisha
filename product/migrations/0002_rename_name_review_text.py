# Generated by Django 5.0.3 on 2024-03-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='text',
        ),
    ]
