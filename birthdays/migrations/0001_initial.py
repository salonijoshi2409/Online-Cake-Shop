# Generated by Django 3.1.6 on 2021-10-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpid', models.CharField(default='none', max_length=10)),
                ('bname', models.CharField(max_length=30)),
                ('bimage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('bdescrip', models.CharField(max_length=100)),
                ('bprice500', models.IntegerField(blank=True, null=True)),
                ('bprice1', models.IntegerField(blank=True, null=True)),
                ('bprice2', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
