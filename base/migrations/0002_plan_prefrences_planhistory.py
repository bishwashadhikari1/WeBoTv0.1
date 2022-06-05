# Generated by Django 4.0.2 on 2022-06-02 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_plan', models.TextField(default='BASIC')),
                ('expiration', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefrences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk', models.FloatField()),
                ('positionSize', models.IntegerField()),
                ('tickerQuantity', models.IntegerField()),
                ('strategy', models.TextField()),
                ('timeFrame', models.IntegerField()),
                ('riskReward', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users')),
            ],
        ),
        migrations.CreateModel(
            name='PlanHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('expiry', models.DateTimeField()),
                ('currency', models.TextField()),
                ('network', models.TextField()),
                ('timePeriod', models.TextField()),
                ('transactionId', models.TextField()),
                ('verified', models.BooleanField()),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.plan')),
            ],
        ),
    ]
