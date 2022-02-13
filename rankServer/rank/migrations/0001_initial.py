# Generated by Django 4.0.2 on 2022-02-13 18:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=16, unique=True, verbose_name='客户端号')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(1)], verbose_name='分数')),
            ],
            options={
                'verbose_name': '分数登记表',
                'verbose_name_plural': '分数登记表',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('c_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='rank.score')),
                ('rank', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='名次')),
            ],
        ),
    ]
