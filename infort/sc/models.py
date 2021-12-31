from django.db import models
from django.urls import reverse

# Главные модели


class Schematic(models.Model):
    """ Модель схем"""
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufactured = models.ForeignKey('Vendor', on_delete=models.PROTECT, verbose_name='Производитель')
    file = models.FileField(upload_to='schematic/', verbose_name='Файл')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Схемы'
        verbose_name_plural = 'Схемы'
        ordering = ['pk']


class Service(models.Model):
    """ Модель сервиса """

    clients = models.ForeignKey('Client', on_delete=models.PROTECT, verbose_name='Клиент')
    devices = models.ForeignKey('Device', on_delete=models.PROTECT, verbose_name='Устройство')
    manufactured = models.ForeignKey('Vendor', on_delete=models.PROTECT, verbose_name='Производитель')
    model = models.CharField(max_length=100, verbose_name='Модель устройства')
    serial = models.CharField(blank=True, max_length=50, verbose_name="Серийный номер")
    bug = models.TextField(verbose_name='Неисправность')
    time_reception = models.DateTimeField(auto_now_add=True)
    stage = models.ForeignKey('Stage', on_delete=models.PROTECT, default=0, verbose_name='Стадия ремонта')
    comment = models.TextField(blank=True, verbose_name='Комментарий инженера')
    service_list = models.ManyToManyField('Service_list', blank=True, verbose_name='Оказанные услуги')

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервис'
        ordering = ['-pk']

    def __str__(self):
        item = 'Номер заказа : ' + str(self.pk)
        return item


# Модели полей


class Vendor(models.Model):
    vendor = models.CharField(max_length=50, verbose_name='Производитель')

    def __str__(self):
        return self.vendor

    def get_absolute_url(self):
        return self.vendor

    class Meta:
        verbose_name = 'Производители'
        verbose_name_plural = 'Производители'
        ordering = ['id']


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя клиента')
    phone = models.IntegerField(verbose_name='Номер телефона')

    def __str__(self):
        return self.name


class Device(models.Model):
    device = models.CharField(max_length=50, verbose_name='Устройство')

    def __str__(self):
        return self.device


class Stage(models.Model):
    stage = models.CharField(max_length=20, verbose_name='Стадия ремонта')
    bs_color = models.CharField(max_length=50, verbose_name='Цвет по категориям боотстрап')
    slug = models.CharField(max_length=50, verbose_name='Слаг')

    def __str__(self):
        return self.stage


class Service_list(models.Model):
    type_service = models.CharField(max_length=100, verbose_name='Вид услуги')
    price = models.IntegerField(verbose_name='Цена услуги')

    def __str__(self):
        return self.type_service
