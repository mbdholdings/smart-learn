# Generated by Django 4.0.1 on 2022-02-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofileinfo_role_alter_userprofileinfo_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slide',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='welcome',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
