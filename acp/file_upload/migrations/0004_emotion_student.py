# Generated by Django 3.0 on 2020-03-24 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0003_auto_20200323_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotion',
            name='student',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to='file_upload.Document'),
        ),
    ]
