# Generated by Django 4.0.1 on 2022-02-13 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_lesson_video_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='video_link',
            new_name='videolink',
        ),
    ]
