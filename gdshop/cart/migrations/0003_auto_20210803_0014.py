# Generated by Django 2.2 on 2021-08-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='quant',
            new_name='quan',
        ),
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
