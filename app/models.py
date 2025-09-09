from .db import db

class Student(db.Model):
    _tablename_="student"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)