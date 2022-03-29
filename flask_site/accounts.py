from flask_site import app, db
from flask_site.forms import LoginForm, RegistrationForm
from flask_site.models import User

from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, flash

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form = form)

@app.route("/login", methods = ["POST"])
def login_submit():
    form = LoginForm()
    if form.validate_on_submit():
        usr = User.query.filter_by(username = form.username.data).first()
        if not usr:
            flash("Error: Username not found")
            return redirect("/login")
        if usr.password == form.password.data:
            login_user(usr)
            return redirect("/tasks")
        else:
            flash("Error: Password does not match with username")
            return redirect("/login")
    else:
        flash("Invalid post request")
        return redirect("/login")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form = form)

@app.route("/register", methods = ["POST"])
def register_submit():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username = form.username.data).first():
            flash("Error: a user with this username already exists")
            return redirect("/register")
        usr = User(username = form.username.data, password = form.password.data)
        db.session.add(usr)
        db.session.commit()
        login_user(usr)
        return redirect("/tasks")
    else:
        flash("Invalid post request")
        return redirect("/register")

@app.route("/logout")
def logout():
    logout_user()
    flash("Successfully logged out. See you later!")
    return redirect("/")
