# Generated by Django 3.1.3 on 2023-10-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
            ],
        ),
    ]
