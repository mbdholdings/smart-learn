# Generated by Django 4.0.1 on 2022-02-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_comment_id_alter_grade_id_alter_lesson_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comm_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
