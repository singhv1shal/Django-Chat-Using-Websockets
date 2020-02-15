# Generated by Django 2.2.3 on 2019-08-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('member', models.EmailField(max_length=254)),
                ('isAuthorized', models.CharField(max_length=2)),
            ],
        ),
    ]