# Generated by Django 3.2.8 on 2021-10-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TextField(default=1635685083.618764),
        ),
    ]
