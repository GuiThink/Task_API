import sqlite3


class CreateDb:
    """
    Creates the Database and Tables if it doesn't exist.
    """

    def __init__(self):
        self.conn = sqlite3.connect('api.db')
        # creates the db on the fly is not exists

        self.c = self.conn.cursor()

    def table_task(self):
        """
        Create table 'task' if not already created.
        """
        self.c.execute(
            'CREATE TABLE IF NOT EXISTS task ('
            'id INTEGER PRIMARY KEY, '
            'shortdesc TEXT NOT NULL, '
            'longdesc TEXT, '
            'state BOOLEAN NOT NULL, '
            'datestamp TEXT)')

    def data_entry(self):
        self.c.execute('INSERT INTO task (shortdesc, state) VALUES ("mon premier truc", False)');


conn = sqlite3.connect('api.db')
# creates the db on the fly is not exists
c = conn.cursor()

def table_task():
    """
    Create table 'task' if not already created.
    """
    c.execute(
        'CREATE TABLE IF NOT EXISTS task ('
        'id INTEGER PRIMARY KEY, '
        'shortdesc TEXT NOT NULL, '
        'longdesc TEXT, '
        'state BOOLEAN NOT NULL, '
        'datestamp TEXT)')


table_task()