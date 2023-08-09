import json, datetime, random
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from faker import Faker


class Command(BaseCommand):
    help = "Generate Mock Data"

    def getSchool(self):
        fake = Faker()
        Faker.seed(random.random())
        current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "model": "RiserAcademicAPI.School",
            "fields": {
                "school_name": fake.name() + ' School',
                "school_type": random.choice(["E", "M", "H", "C"]),
                "school_city": fake.city(),
                "school_state": fake.state(),
                "created_at": current_timestamp,
                "updated_at": current_timestamp
            }
        }

    def getCourse(self, school_count):
        fake = Faker()
        while 1:
            Faker.seed(random.random())
            fake_job = fake.job()
            if len(fake_job) < 20:
                break
        current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "model": "RiserAcademicAPI.Course",
            "fields": {
                "course_code": fake_job + " " + str(random.randrange(1, 299)),
                "course_name": fake.paragraph(nb_sentences=1),
                "course_room": fake.name() + " " + str(random.randrange(101, 999)),
                "school_id": random.randrange(1, school_count),
                "teacher_id": random.randrange(1, 10),
                "created_at": current_timestamp,
                "updated_at": current_timestamp
            }
        }

    def handle(self, *args, **options):
        school_count = random.randrange(10, 30)
        course_count = random.randrange(50, 100)
        data = []
        [data.append(self.getSchool()) for _ in range(school_count)]
        [data.append(self.getCourse(school_count)) for _ in range(course_count)]
        data = json.dumps(data)

        with open("sample_fixture.json", "w") as f:
            file_handler = File(f)
            file_handler.write(data)
