from app import Course, db, Student, app

def add_student(f_name, l_name, email, phone):
    new_student = Student(f_name=f_name, l_name=l_name, email=email, phone=phone)
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
        add_student(f_name='Nkurikiyimana', l_name='Aimable', email='nkurikiyimana@gmail.com', phone='+250783000111')
        #delete_student(email='elyse150@gmail.com')