# Generated by Django 2.2 on 2020-09-10 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, verbose_name='Токен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('life_days', models.IntegerField(default=7, verbose_name='Срок действия (в днях)')),
                ('type', models.CharField(choices=[('register', 'Регистрация'), ('password_reset', 'Восстановление пароля')], default='register', max_length=20, verbose_name='Тип токена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Аутентификационный токен',
                'verbose_name_plural': 'Аутентификационные токены',
            },
        ),
    ]
