# Generated by Django 4.2.10 on 2024-03-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllerEmail', '0011_emailtracker_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtracker',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='email_documents/'),
        ),
    ]
