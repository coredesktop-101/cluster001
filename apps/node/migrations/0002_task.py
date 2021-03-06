# Generated by Django 3.0.5 on 2020-04-08 14:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('duration', models.CharField(max_length=32)),
                ('dependencies', models.CharField(max_length=32)),
                ('resources', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
