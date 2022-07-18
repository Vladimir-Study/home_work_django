import csv
from slugify import slugify

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            slug_text = slugify(phone['name'])
            write_phone = Phone(name=f"{phone['name']}", image=f"{phone['image']}",
                                price=f"{int(phone['price'])}", release_date=f"{phone['release_date']}",
                                lte_exists=f"{phone['lte_exists']}", slug=slug_text)
            write_phone.save()
