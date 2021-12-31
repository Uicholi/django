# Generated by Django 3.2.9 on 2021-12-07 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0002_auto_20211126_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя клиента')),
                ('phone', models.IntegerField(max_length=12, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=50, verbose_name='Устройство')),
            ],
        ),
        migrations.CreateModel(
            name='Service_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_service', models.CharField(max_length=100, verbose_name='Вид услуги')),
                ('price', models.IntegerField(verbose_name='Цена услуги')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=20, verbose_name='Стадия ремонта')),
            ],
        ),
        migrations.AlterModelOptions(
            name='schematic',
            options={'ordering': ['pk'], 'verbose_name': 'Схемы', 'verbose_name_plural': 'Схемы'},
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Модель устройства')),
                ('serial', models.CharField(blank=True, max_length=50, verbose_name='Серийный номер')),
                ('bug', models.TextField(verbose_name='Неисправность')),
                ('time_reception', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий инженера')),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sc.client', verbose_name='Клиент')),
                ('devices', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sc.device', verbose_name='Устройство')),
                ('manufactured', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sc.vendor', verbose_name='Производитель')),
                ('service_list', models.ManyToManyField(to='sc.Service_list', verbose_name='Оказанные услуги')),
                ('stage', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='sc.stage', verbose_name='Стадия ремонта')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервис',
                'ordering': ['-pk'],
            },
        ),
    ]
