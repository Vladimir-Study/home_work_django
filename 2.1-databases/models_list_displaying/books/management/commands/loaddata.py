from django.core.management.base import BaseCommand
from slugify import slugify

from books.models import Book
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(options['path'], 'r', encoding='utf-8') as file:
            dict_json = json.load(file)
            for line in dict_json:
                slug_text = slugify(line['fields']['pub_date'])
                write_book = Book(
                    name = f"{line['fields']['name']}",
                    author = f"{line['fields']['author']}",
                    pub_date=f"{line['fields']['pub_date']}",
                    slug=slug_text,
                )
                write_book.save()

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            action='store'
        )
