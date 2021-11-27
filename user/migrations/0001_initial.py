# Generated by Django 3.2.9 on 2021-11-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.TextField(blank=True)),
                ('updated_at', models.TextField(blank=True)),
                ('userid', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
