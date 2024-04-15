from app import Course, db, Student, app
import random

def add_student(f_name, l_name, email, phone):
    new_student = Student(f_name=f_name, l_name=l_name, email=email, phone=phone, cohort=random.randint(1,3))
    db.session.add(new_student)
    db.session.commit()

def delete_student(email):
    student = Student.query.filter_by(email=email).first()
    db.session.delete(student)
    db.session.commit()

def add_course(course_name):
    if course_name:
        new_course = Course(course_name=course_name)
        db.session.add(new_course)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        n = 0
        while n < 50:
            add_student(f_name=f'first_student{n}', l_name='als_student'+f'{n}', email='email'+f'{n}'+'@gmail.com', phone=f'+25078000{n}')
            n += 1
            
        # courses = [
        #     'Software engineering',
        #     'Data science',
        #     'Data analytics',
        #     'Aws cloud computing',
        #     'Salesforce administration',
        #     'Ai career essential'
        #     ]
        # for course in courses:
        #     add_course(course)