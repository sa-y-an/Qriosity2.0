# Generated by Django 3.0.7 on 2020-06-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200628_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerdetails',
            name='name_user',
        ),
    ]
