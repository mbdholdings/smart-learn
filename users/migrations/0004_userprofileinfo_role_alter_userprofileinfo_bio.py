# Generated by Django 4.0.1 on 2022-02-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_welcome'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='role',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]