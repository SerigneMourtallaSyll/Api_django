# Generated by Django 4.2.10 on 2024-03-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllerEmail', '0008_emailtracking_opened_at_alter_emailtracker_opened_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_at', models.CharField(max_length=255)),
            ],
        ),
    ]
