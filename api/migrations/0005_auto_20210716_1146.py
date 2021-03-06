# Generated by Django 3.1.6 on 2021-07-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210715_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100, null=True)),
                ('area_address', models.TextField(max_length=200, null=True)),
                ('area_type', models.CharField(choices=[('1', 'restaurant'), ('2', 'pubs'), ('3', 'offices')], max_length=10, null=True)),
                ('area_capacity', models.IntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RenameModel(
            old_name='Register',
            new_name='UserRegister',
        ),
    ]
