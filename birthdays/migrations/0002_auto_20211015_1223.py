# Generated by Django 3.1.6 on 2021-10-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='bpid',
            field=models.CharField(default='none', max_length=10, unique=True),
        ),
    ]