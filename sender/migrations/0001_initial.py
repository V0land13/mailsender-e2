# Generated by Django 3.0.3 on 2020-02-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailForSend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailer', models.EmailField(help_text='Введите Email получателя', max_length=254)),
                ('subject', models.CharField(help_text='Тема письма, не более 50 знаков.', max_length=50)),
                ('text', models.TextField()),
                ('sec_to_send', models.BigIntegerField()),
                ('is_send', models.BooleanField(default=False)),
            ],
        ),
    ]
