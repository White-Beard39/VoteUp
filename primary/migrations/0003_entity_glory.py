# Generated by Django 5.1.2 on 2024-11-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0002_alter_entity_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='glory',
            field=models.BigIntegerField(default=0),
        ),
    ]