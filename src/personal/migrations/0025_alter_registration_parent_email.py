# Generated by Django 5.1.7 on 2025-05-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0024_alter_highlighted_speaker_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='parent_email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name="Parent's Email"),
        ),
    ]
