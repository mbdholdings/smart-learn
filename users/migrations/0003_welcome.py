# Generated by Django 4.0.1 on 2022-02-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=200, null=True)),
                ('title2', models.CharField(blank=True, max_length=200, null=True)),
                ('motto', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
