# Generated by Django 2.1 on 2018-12-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]
