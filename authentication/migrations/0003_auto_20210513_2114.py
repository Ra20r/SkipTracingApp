# Generated by Django 2.2.10 on 2021-05-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210512_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='available_skipTraces',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pending_skipTraces',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_orders',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_skipTraces',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_spent',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
    ]