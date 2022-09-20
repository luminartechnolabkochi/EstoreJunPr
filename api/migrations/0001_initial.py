# Generated by Django 3.2.15 on 2022-09-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('publisher', models.CharField(max_length=200)),
            ],
        ),
    ]
