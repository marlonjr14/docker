from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = "Generate initial data with Faker"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # --- Colleges ---
        colleges = []
        for i in range(8):
            college = College.objects.create(college_name=fake.company())
            colleges.append(college)
        self.stdout.write(self.style.SUCCESS("Created 8 Colleges"))

        # --- Programs ---
        programs = []
        for i in range(10):
            program = Program.objects.create(
                prog_name=fake.job(),
                college=random.choice(colleges)
            )
            programs.append(program)
        self.stdout.write(self.style.SUCCESS("Created 10 Programs"))

        # --- Organizations ---
        orgs = []
        for i in range(10):
            org = Organization.objects.create(
                name=fake.word().capitalize() + " Org",
                college=random.choice(colleges),
                description=fake.sentence()
            )
            orgs.append(org)
        self.stdout.write(self.style.SUCCESS("Created 10 Organizations"))

        # --- Students ---
        students = []
        for i in range(50):
            student = Student.objects.create(
                student_id=f"2025-{1000+i}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.first_name() if random.choice([True, False]) else None,
                program=random.choice(programs)
            )
            students.append(student)
        self.stdout.write(self.style.SUCCESS("Created 50 Students"))

        # --- Org Members ---
        for i in range(10):
            OrgMember.objects.create(
                student=random.choice(students),
                organization=random.choice(orgs),
                date_joined=timezone.now() - timedelta(days=random.randint(0, 730))
            )
        self.stdout.write(self.style.SUCCESS("Created 10 Org Members"))