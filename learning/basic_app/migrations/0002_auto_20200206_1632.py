# Generated by Django 3.0 on 2020-02-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='hello',
        ),
    ]
