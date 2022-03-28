from flask_site import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(20), nullable = False)

    tasks = db.relationship("Task", backref = "owner", lazy = True)

    def __repr__(self):
        return f"(id: {self.id}, username: {self.username}, password: {self.password})"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text, nullable = False)

    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"({self.id}, {self.content}, {self.date_created}, {self.owner})"