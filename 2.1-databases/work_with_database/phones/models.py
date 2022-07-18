from django.db import models
from django.urls import reverse


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=255, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена')
    image = models.CharField(max_length=500, verbose_name='Фото')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(default=True, verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
