# Generated by Django 4.0.2 on 2022-06-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.TextField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('api_key', models.TextField(max_length=100, unique=True)),
                ('api_secret', models.TextField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
