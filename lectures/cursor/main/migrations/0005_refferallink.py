# Generated by Django 4.2.1 on 2023-06-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_orderitems_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefferalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refferal_link', models.CharField(max_length=45, unique=True)),
                ('count_of_view', models.BigIntegerField()),
            ],
        ),
    ]
