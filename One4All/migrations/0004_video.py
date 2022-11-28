# Generated by Django 3.2.16 on 2022-11-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20221109_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'video',
                'managed': False,
            },
        ),
    ]