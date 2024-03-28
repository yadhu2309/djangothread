import threading
from .models import *

from faker import Faker
fake = Faker()
import random

class CreateStudentThread(threading.Thread):
    def __init__(self, num_stud):
        self.num_stud = num_stud
        threading.Thread.__init__(self)

    def run(self):
        try:
            for i in range(self.num_stud):
                print(i)
                Students.objects.create(name=fake.first_name(),
                                    emial=fake.email(),
                                    age=random.randint(10, 50))
        except Exception as e:
            print(e)