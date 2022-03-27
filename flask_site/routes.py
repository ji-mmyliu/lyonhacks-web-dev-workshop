from flask_site import app
from flask_site.models import User, Task

from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

