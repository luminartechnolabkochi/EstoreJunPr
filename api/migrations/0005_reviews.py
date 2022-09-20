# Generated by Django 3.2.15 on 2022-09-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_books_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=120)),
                ('user', models.CharField(max_length=120)),
                ('comment', models.CharField(max_length=140)),
                ('rating', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]