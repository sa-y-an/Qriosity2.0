# Generated by Django 3.0.7 on 2020-06-28 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200628_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerdetails',
            name='name_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Player'),
        ),
    ]
