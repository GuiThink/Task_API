import sqlite3
from task import Task
from db_conn_alchemy import *

conn = sqlite3.connect('task.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS tasks (
            title TEXT,
            description TEXT,
            owner TEXT,
            priority INTEGER,
            project TEXT,
            epic TEXT,
            end_date TEXT,
            state INTEGER,
            creation_date TEXT
            )""")


def insert_task(task):
    with conn:
        c.execute("INSERT INTO tasks "
                  "VALUES ("
                  ":title, "
                  ":description, "
                  ":owner, "
                  ":priority, "
                  ":project, "
                  ":epic, "
                  ":end_date, "
                  ":state, "
                  ":creation_date"
                  ")",
                  {'title': task.title,
                   'description': task.description,
                   'owner': task.owner,
                   'priority': task.priority,
                   'project': task.project,
                   'epic': task.epic,
                   'end_date': task.end_date,
                   'state': task.state,
                   'creation_date': task.creation_date
                   }
                  )


def get_tasks():
    with conn:
        c.execute("SELECT * FROM tasks")
        return c.fetchall()


def get_task(id):
    pass


def update_task(id):
    pass


def delete_task(id):
    pass


task_1 = Task('Apprendre Python')
task_2 = Task('Manger des bonbons', 'Aller à Carrouf pour acheter des bonbons et en manger plein !', 'Jiji', '2', 'Grossir v2.0', 'Achats', '2018-03-07', 'to do')
task_3 = Task('Retirer des sous', 'Retirer 300 euros à la banque pour les achats de bonbons', 'Guillaume', '1', 'Grossir v2.0', 'Achats', '2018-03-06', 'en cours')


insert_task(task_1)
insert_task(task_2)
insert_task(task_3)




# c.execute("INSERT INTO tasks VALUES (1, 'Learn Python', 'You should learn Python', 1, '2018-03-02')")
#
# c.execute("SELECT * FROM tasks")
# print(c.fetchall())

conn.commit()
conn.close()

