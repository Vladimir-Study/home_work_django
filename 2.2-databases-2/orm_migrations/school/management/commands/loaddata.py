from django.core.management.base import BaseCommand
from school.models import Teacher, Student
import json

class Command(BaseCommand):


    def handle(self, *args, **options):
        with open(options['path'], 'r', encoding='utf-8') as file:
            dict_json = json.load(file)
            for line in dict_json:
                if line['model'] == 'school.teacher':
                    write_teacher = Teacher(
                        name = f"{line['fields']['name']}",
                        subject = f"{line['fields']['subject']}",
                    )
                    write_teacher.save()
                elif line['model'] == 'school.student':
                    write_student = Student(
                        name = f"{line['fields']['name']}",
                        group = f"{line['fields']['group']}"
                    )
                    write_student.save()
                    teacher = Teacher.objects.get(pk=line['fields']['teacher'])
                    write_student.teacher.add(teacher)
    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            action='store'
        )
