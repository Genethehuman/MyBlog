# Generated by Django 3.2.10 on 2021-12-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='Add your text here'),
        ),
    ]
