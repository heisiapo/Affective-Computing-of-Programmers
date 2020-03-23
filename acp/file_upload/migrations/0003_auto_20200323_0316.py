# Generated by Django 3.0 on 2020-03-22 19:16

from django.db import migrations, models
import file_upload.validators


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_emotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[file_upload.validators.validate_file_extension]),
        ),
    ]