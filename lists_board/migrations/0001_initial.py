# Generated by Django 2.2.7 on 2019-11-25 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('no', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(max_length=30)),
                ('hits', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]