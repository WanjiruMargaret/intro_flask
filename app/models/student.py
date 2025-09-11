from app.db import db
from datetime import datetime,timezone

def uct_now():
    return datetime.now(timezone.utc)

class Student(db.model):
    _tablename_ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(500), unique=True, nullable=False)
    created_at=db.Column(db.DateTime(timezone=True),default=uct_now,nullable=False)