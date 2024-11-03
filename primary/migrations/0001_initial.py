# Generated by Django 5.1.2 on 2024-11-02 09:47

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('19dcc2b6-8389-4f09-b10a-4cc8e9795f51'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.ManyToManyField(related_name='entity_category', to='primary.category')),
            ],
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='voted_category', to='primary.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voted_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
