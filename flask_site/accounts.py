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
            flash("Username not found")
            return redirect("/")
        if usr.password == form.password.data:
            login_user(usr)
            flash(f"Successfully logged in as {form.username.data}")
            return redirect("/")
        else:
            flash("Incorrect password")
            return redirect("/")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form = form)

@app.route("/register", methods = ["POST"])
def register_submit():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username = form.username.data).first():
            flash("A user with this username already exists")
            return redirect("/")
        usr = User(username = form.username.data, password = form.password.data)
        db.session.add(usr)
        db.session.commit()
    flash(f"Successfully registered account as {usr.username}")
    return redirect("/")

@app.route("/logout")
def logout():
    logout_user()
    flash("Successfully logged out", "success")
    return redirect("/")
