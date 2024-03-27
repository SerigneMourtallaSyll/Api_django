# Generated by Django 4.2.10 on 2024-03-27 00:16

import controllerEmail.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllerEmail', '0015_document_image_remove_emailtracker_document_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtracker',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='emailtracker',
            name='images',
        ),
        migrations.AddField(
            model_name='emailtracker',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=controllerEmail.models.document_upload_path),
        ),
        migrations.AddField(
            model_name='emailtracker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=controllerEmail.models.image_upload_path),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]