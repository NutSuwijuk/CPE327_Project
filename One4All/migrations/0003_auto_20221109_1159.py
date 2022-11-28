# Generated by Django 3.2.16 on 2022-11-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_paymentmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('name_food', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('urls_food', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'food',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField()),
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
    ]