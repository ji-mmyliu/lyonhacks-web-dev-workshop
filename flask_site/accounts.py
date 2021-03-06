from flask_site import app, db
from flask_site.forms import LoginForm, RegistrationForm
from flask_site.models import User

from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, flash

import bcrypt

@app.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect("/")

    form = LoginForm()
    return render_template("login.html", form = form)

@app.route("/login", methods = ["POST"])
def login_submit():
    if current_user.is_authenticated:
        return redirect("/")

    form = LoginForm()
    if form.validate_on_submit():
        usr = User.query.filter_by(username = form.username.data).first()
        if not usr:
            flash("Error: Username not found")
            return redirect("/login")
        if bcrypt.checkpw(form.password.data.encode(), usr.password):
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
    if current_user.is_authenticated:
        return redirect("/")

    form = RegistrationForm()
    return render_template("register.html", form = form)

@app.route("/register", methods = ["POST"])
def register_submit():
    if current_user.is_authenticated:
        return redirect("/")

    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username = form.username.data).first():
            flash("Error: a user with this username already exists")
            return redirect("/register")
        if form.password.data != form.confirm_password.data:
            flash("Error: password confirmation does not match")
            return redirect("/register")
        
        hashed = bcrypt.hashpw(form.password.data.encode(), bcrypt.gensalt())
        usr = User(username = form.username.data, password = hashed)
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
