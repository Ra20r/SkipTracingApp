# Generated by Django 2.2.10 on 2021-05-12 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(blank=True)),
                ('order_type', models.CharField(blank=True, max_length=100)),
                ('total_address', models.IntegerField(blank=True)),
                ('total_hits', models.IntegerField(blank=True)),
                ('hit_percentage', models.CharField(blank=True, max_length=100)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='history', to='authentication.Profile')),
            ],
        ),
    ]
