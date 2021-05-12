# Generated by Django 2.2.10 on 2021-05-12 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.IntegerField(blank=True)),
                ('phone', models.IntegerField(blank=True)),
                ('total_skipTraces', models.IntegerField(blank=True)),
                ('total_orders', models.IntegerField(blank=True)),
                ('total_spent', models.FloatField(blank=True)),
                ('pending_skipTraces', models.IntegerField(blank=True)),
                ('available_skipTraces', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
