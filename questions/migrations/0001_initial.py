# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 21:47
from __future__ import unicode_literals

import common.utilities
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('answer_rep', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(null=True, on_delete=models.SET(common.utilities.get_null_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='AnswerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Answer')),
                ('creator', models.ForeignKey(null=True, on_delete=models.SET(common.utilities.get_null_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Answer comment',
                'verbose_name_plural': 'Answer comments',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('content', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now=True)),
                ('activity', models.DateTimeField(auto_now=True)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('question_rep', models.IntegerField(default=0)),
                ('answers_count', models.IntegerField(default=0)),
                ('views_count', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(null=True, on_delete=models.SET(common.utilities.get_null_user), to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(null=True, on_delete=models.SET(common.utilities.get_null_user), to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
            options={
                'verbose_name': 'Question comment',
                'verbose_name_plural': 'Question comments',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
    ]