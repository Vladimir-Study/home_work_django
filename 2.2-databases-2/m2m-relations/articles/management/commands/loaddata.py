from django.core.management.base import BaseCommand
from articles.models import Article
import json

class Command(BaseCommand):


    def handle(self, *args, **options):
        with open(options['path'], 'r', encoding='utf-8') as file:
            dict_json = json.load(file)
            for line in dict_json:
                write_article = Article(
                    title = f"{line['fields']['title']}",
                    text = f"{line['fields']['text']}",
                    published_at = f"{line['fields']['published_at']}",
                    image = f"{line['fields']['image']}",
                )
                write_article.save()

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            action='store'
        )
