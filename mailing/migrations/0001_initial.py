# Generated by Django 4.2 on 2024-06-10 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Начало рассылки')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Конец рассылки')),
                ('sending', models.CharField(choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], max_length=50, verbose_name='Период рассылки')),
                ('setting_status', models.CharField(choices=[('Create', 'Создана'), ('Started', 'Отправлено'), ('Done', 'Завершена')], default='Create', max_length=50, verbose_name='Статус рассылки')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmessage', verbose_name='Сообщения')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройки рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_datetime', models.DateTimeField(auto_now_add=True, verbose_name='last_datetime')),
                ('status', models.CharField(choices=[('success', 'успешно'), ('fail', 'неуспешно')], default='', max_length=50, verbose_name='статус попытки')),
                ('mailing_response', models.TextField(verbose_name='mailing_response')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'Статус отправки',
                'verbose_name_plural': 'Статусы отправки',
            },
        ),
    ]
