# Generated by Django 3.1.6 on 2021-07-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210715_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='photo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]