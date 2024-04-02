#!/usr/bin/python3
"""this is the flasj implimentation of the database"""
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# model definition
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))
    students = db.relationship('Student', backref='course', lazy=True)

# class Cohort(db.Model):
#     id = db.column(db.Integer, primary_key=True)
#     cohort = f'{Course.course_name} + {cohort_number}'

with app.app_context():
    db.create_all()
    

# Routes

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    output = []
    for student in students:
        student_data = {
            'id': student.id,
            'f_name': student.f_name,
            'l_name': student.l_name,
            'email': student.email,
            'phone': student.phone,
            'course_id': student.course_id
        }
        output.append(student_data)
    return jsonify({'students': output})

# post method to add at the datbase
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    new_student = Student(
        f_name=data['first_name'],
        l_name=data['last_name'],
        email=data['email'],
        phone=data['phone'],
        course_id=data['course_id']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully!'}), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    output = []
    for course in courses:
        course_data = {
            'id': course.id,
            'course_name': course.course_name
        }
        output.append(course_data)
    return jsonify({'courses': output})

# add the course
@app.route('/courses', methods=['POST'])
def add_course():
    data = request.json
    new_course = Course(
        course_name=data['course_name']
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message':'course successfully added'}), 201
        

if __name__ == '__main__':
    app.run(port=8080, debug=True)
