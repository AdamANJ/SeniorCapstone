# Generated by Django 5.1.7 on 2025-04-26 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_alter_imagecontainer_options_imagecontainer_welcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='speakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=400, upload_to='media/speakers/', width_field=400)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
        ),
    ]
