# Generated by Django 2.0.5 on 2018-06-30 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20180630_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulepost',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
