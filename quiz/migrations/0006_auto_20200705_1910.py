# Generated by Django 3.0.7 on 2020-07-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200704_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagetwo',
            name='level',
            field=models.IntegerField(default=-1),
        ),
    ]
