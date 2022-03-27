from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(20), nullable = False)

    tasks = db.relationship("Task", backref = "owner", lazy = True)

    def __repr__(self):
        return f"(id: {self.id}, username: {self.username}, password: {self.password})"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text, nullable = False)

    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    date_due = db.Column(db.DateTime, default = datetime.utcnow)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"({self.id}, {self.content}, {self.date_created}, {self.date_due}, {self.owner})"