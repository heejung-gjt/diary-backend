# Generated by Django 3.2.8 on 2021-10-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_alter_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.TextField(default=1635685057.8501081),
        ),
    ]
