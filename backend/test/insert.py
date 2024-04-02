#!/usr/bin/python3
from fabric import task
from faker import Faker
import random

fake = Faker()

@task
def add_data(c):
    """Add 20 sets of random data to the database"""
    for _ in range(20):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        country_origin = fake.country()
        phone = fake.phone_number()
        course_id = random.randint(1, 5)  # Assuming there are 5 courses

        add_student(c, first_name, last_name, email, country_origin, phone, course_id)

@task
def add_student(c, first_name, last_name, email, country_origin, phone, course_id):
    """Add a new student to the database"""
    command = f'sqlite3 ../peers.db "INSERT INTO students (first_name, last_name, email, country_origin, phone, course_id) VALUES (\'{first_name}\', \'{last_name}\', \'{email}\', \'{country_origin}\', \'{phone}\', \'{course_id}\');"'
    c.run(command)
