from student_db import app, db, Student, Course
import random

def add_students(num_students):
    for _ in range(num_students):
        student = Student(
            f_name='Student{}'.format(_),
            l_name='Lastname{}'.format(_),
            email='student{}@example.com'.format(_),
            phone='123456789{}'.format(random.randint(0, 9)),
            course_id=random.randint(1, 5),
            password='password'
        )
        db.session.add(student)
    db.session.commit()

def add_courses(num_courses):
    for _ in range(num_courses):
        course = Course(
            course_name='Course{}'.format(_)
        )
        db.session.add(course)
    db.session.commit()

if __name__ == '__main__':
    num_students = 20
    num_courses = 5
    
    with app.app_context():
        add_courses(num_courses)
        add_students(num_students)
