# Generated by Django 3.2.17 on 2023-02-11 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_login', models.CharField(max_length=50, unique=True, verbose_name='Логин')),
                ('socials', models.CharField(blank=True, max_length=50, null=True, verbose_name='Jabber/telegram')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25, unique=True, verbose_name='Номер')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('thema', models.CharField(max_length=50, verbose_name='Тема')),
                ('answers', models.CharField(max_length=50, verbose_name='Ответов')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Тикет',
                'verbose_name_plural': 'Тикеты',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25, unique=True, verbose_name='Номер')),
                ('item', models.CharField(max_length=25, verbose_name='Товар')),
                ('city', models.CharField(max_length=25, verbose_name='Город')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('payment_method', models.CharField(max_length=25, verbose_name='Метод оплаты')),
                ('date', models.DateTimeField(verbose_name='Дата покупки')),
                ('found', models.BooleanField(default=False, verbose_name='Найден')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='MyPaidTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25, unique=True, verbose_name='Номер')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('amount', models.IntegerField(verbose_name='Сумма')),
                ('total_amount', models.IntegerField(verbose_name='К оплате')),
                ('requisites', models.CharField(max_length=100, verbose_name='Реквизиты')),
                ('method', models.CharField(max_length=50, verbose_name='Метод')),
                ('type_process', models.CharField(max_length=50, verbose_name='Тип процедуры')),
                ('in_place', models.BooleanField(default=False, verbose_name='Зачислен')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]