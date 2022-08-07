from django.db import models
from django.utils import timezone

class Measurement(models.Model):

    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements',
                                    verbose_name='Измерения', blank=True)
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(editable=False, verbose_name='Время последнего замера')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now() 
        self.created_at = timezone.now() 
        return super(Measurement, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения' 
        
    def __str__(self):
        return f'{self.temperature}'

class Sensor(models.Model):

    name = models.CharField(max_length=50, verbose_name='Имя датчика')
    description = models.TextField(max_length=500, verbose_name='Описание датчика')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return f'{self.description}: {self.name}'