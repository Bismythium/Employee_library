# Generated by Django 2.2.1 on 2019-06-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siteuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, verbose_name='Username')),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
