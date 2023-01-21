# Generated by Django 3.1.7 on 2023-01-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='irisModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.FloatField(blank=True, default=0)),
                ('sepal_width', models.FloatField(blank=True, default=0)),
                ('petal_length', models.FloatField(blank=True, default=0)),
                ('petal_width', models.FloatField(blank=True, default=0)),
                ('species', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
    ]
