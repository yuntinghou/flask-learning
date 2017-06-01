from app import app
from app.models import Todo
from flask import render_template

@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)
