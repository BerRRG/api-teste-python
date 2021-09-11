# Generated by Django 3.2.7 on 2021-09-09 14:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('reviewScore', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
