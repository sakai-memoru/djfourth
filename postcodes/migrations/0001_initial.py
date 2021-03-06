# Generated by Django 2.0.6 on 2018-06-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jisx0401', models.CharField(max_length=5)),
                ('post_code5', models.CharField(max_length=3)),
                ('post_code', models.CharField(max_length=7, unique=True)),
                ('prefecture_kana', models.CharField(max_length=30)),
                ('city_kana', models.CharField(max_length=30)),
                ('town_kana', models.CharField(max_length=30)),
                ('prefecture', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=2000)),
                ('flag_1', models.CharField(max_length=1, null=True)),
                ('flag_2', models.CharField(max_length=1, null=True)),
                ('flag_3', models.CharField(max_length=1, null=True)),
                ('flag_4', models.CharField(max_length=1, null=True)),
                ('flag_5', models.CharField(max_length=1, null=True)),
                ('reason_for_update', models.CharField(max_length=1, null=True)),
            ],
        ),
    ]
