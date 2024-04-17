from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from random import choice, randint
from app import Course, db, Student, app

# Assuming your Flask and SQLAlchemy setup is as above

# List of courses
courses = ['Software engineering', 'Data science', 'Data analytics', 'Aws cloud computing', 'Salesforce administration', 'Ai career essential']

# Function to add students
def add_students():
    for i in range(50):
        # Randomly select a course for the student
        course_name = choice(courses)
        course = Course.query.filter_by(course_name=course_name).first()

        # Create a new student
        student = Student(
            f_name=f'Student{i}',
            l_name=f'LastName{i}',
            email=f'student{i}@example.com',
            phone=f'123-456-78{i}',
            course_id=course.id,
            cohort= randint(1,3),
            # password='password'
        )

        # Add the student to the session and commit it
        db.session.add(student)
        db.session.commit()

# Run the function to add students
if __name__ == '__main__':
    with app.app_context():
        add_students()