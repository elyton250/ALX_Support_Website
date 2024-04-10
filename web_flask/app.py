# from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from os import getenv
from dotenv import load_dotenv
"""My Flask App"""


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(
         getenv("DB_USER"),
         getenv("DB_PASS"),
         getenv("DB_HOST"),
         getenv("DB_NAME")
    )
"""initializing database"""
db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(100))
#     image_file = db.Column(db.String(50), nullable=False, default='default.png')
#     sermons = db.relationship('Sermon', backref='author', lazy=True)

# class Sermon(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     verse = db.Column(db.String(50), nullable=False)
#     audio_file = db.Column(db.String(50), nullable=False, unique=True)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow().date)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    image_file = db.Column(db.String(50), nullable=False, default='default.png')
    phone = db.Column(db.String(20), nullable=False, unique=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    password=db.Column(db.String(256))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False, unique=True)
    students = db.relationship('Student', backref='course', lazy=True)

"""create tables in the database"""
with app.app_context():
    db.create_all()

from routes import *


if __name__ == "__main__":
    """create tables in database"""
    app.run(host='0.0.0.0', port=8000, debug=True)