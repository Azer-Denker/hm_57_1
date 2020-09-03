# Generated by Django 2.2 on 2020-09-03 08:50

from django.db import migrations, models
import django.db.models.deletion
import webapp.validate


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=50, verbose_name='Название')),
                ('description', models.TextField(default='None', max_length=300, verbose_name='Описание')),
                ('starts_date', models.DateField(verbose_name='дата начала')),
                ('finish_date', models.DateField(blank=True, null=True, verbose_name='дата окончания')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'Новая'), ('In_progress', 'В процессе'), ('Done', 'Сделано')], default='New', max_length=300, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Issue', 'Задача'), ('Bug', 'Ошибка'), ('Enhancement', 'Улучшение')], default='Issue', max_length=300, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(default='None', max_length=300, validators=[webapp.validate.title], verbose_name='Задание')),
                ('description', models.TextField(blank=True, default='None description', max_length=3500, null=True, validators=[webapp.validate.null], verbose_name='Описание')),
                ('completion_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue', to='webapp.Project', verbose_name='Проект')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue', to='webapp.Status', verbose_name='Статус')),
                ('type', models.ManyToManyField(related_name='type', to='webapp.Type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
