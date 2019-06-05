# Generated by Django 2.2.1 on 2019-05-30 23:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.IntegerField(auto_created = True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('date_deposited', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]