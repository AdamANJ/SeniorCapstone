# Generated by Django 5.1.7 on 2025-04-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0019_alter_speaker_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlighted_speaker',
            name='image',
            field=models.ImageField(upload_to='media/highlighted_speakers/'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.ImageField(upload_to='media/speakers/'),
        ),
    ]
