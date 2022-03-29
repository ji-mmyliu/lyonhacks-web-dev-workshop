from flask_site import app, db
from flask_site.forms import CreateTaskForm
from flask_site.models import User, Task
from flask_login import login_required

from flask import render_template, redirect, flash
from flask_login import current_user

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect("/tasks")
    else:
        return redirect("/login")

@app.route('/tasks')
@login_required
def tasks():
    form = CreateTaskForm()
    return render_template("tasks.html", form = form, tasks = Task.query.filter_by(owner = current_user))

@app.route('/tasks/new', methods = ["POST"])
@login_required
def new_task_submit():
    form = CreateTaskForm()
    if form.validate_on_submit():
        new_task = Task(content = form.content.data, owner_id = current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return redirect("/tasks")

@app.route('/tasks/<int:task_id>/delete', methods = ["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id = task_id).first()
    if current_user != task.owner:
        flash("You do not have permission to delete this task")
        return redirect("/tasks")
    db.session.delete(task)
    db.session.commit()
    flash(f"Successfully deleted task {task_id}")
    return redirect("/tasks")