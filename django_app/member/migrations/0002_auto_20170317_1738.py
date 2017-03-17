# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 08:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.IntegerField(choices=[(1, 'Follow'), (2, 'Block')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='relation',
            field=models.ManyToManyField(related_name='relation_user_set', through='member.Relationship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='relationship',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
