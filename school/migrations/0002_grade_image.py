# Generated by Django 4.0.1 on 2022-02-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/'),
        ),
    ]