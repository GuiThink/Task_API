from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default="datetime.utcnow")
    end_date = db.Column(db.DateTime, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    state = db.Column(db.Integer, db.ForeignKey('state.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    identifier = db.Column(db.String(5), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='owner')
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=True)
    identifier = db.Column(db.String(5), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='project')


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    identifier = db.Column(db.String(5), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    members = db.relationship('User', backref='team')


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='priority')


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='type')


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='state')


@app.route("/todo/api/v1.0/tasks")
#TODO: create route to retrieve all tasks
def get_tasks():
    return "All tasks"


@app.route("/todo/api/v1.0/tasks/<int:task_id>")
#TODO: create route to retrieve a task by id
def get_task(task_id):
    return f'Task id {task_id}'


@app.route("/todo/api/v1.0/task", methods=['POST'])
#TODO: create route to create a new task
def create_task():
    return "New task"


@app.route("/todo/api/v1.0/tasks", methods=['PUT'])
#TODO: create route to modify a task by id
def modify_task():
    return "Modified task"


@app.route("/todo/api/v1.0/tasks", methods=['DELETE'])
#TODO: create route to delete a task by id
def delete_task():
    return "Task deleted"


if __name__ == '__main__':
    app.run(debug=True)