# Generated by Django 4.2.10 on 2024-03-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllerEmail', '0003_email_delete_trackingdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('counter_is', models.CharField(blank=True, max_length=242, null=True)),
                ('unique_code', models.UUIDField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
