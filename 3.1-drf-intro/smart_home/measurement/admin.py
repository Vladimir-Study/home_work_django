from django.contrib import admin
from .models import Measurement, Sensor

# Register your models here.
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'temperature']
    readonly_fields = ['created_at']


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']