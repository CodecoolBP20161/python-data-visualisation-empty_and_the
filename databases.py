import psycopg2
import subprocess
from csvfiles import CSVfiles


class Databases:

    def __init__(self, filename, table_name):
        self.filename = filename
        self.table_name = table_name
        self.dbname = CSVfiles(self.filename).get_data()[0]
        self.username = CSVfiles(self.filename).get_data()[1]
        self.host = CSVfiles(self.filename).get_data()[2]
        self.password = CSVfiles(self.filename).get_data()[3]
        self.connect_str = "dbname={0} user={1} host={2} password={3}".format(self.dbname, self.username, self.host,
                                                                              self.password)
        self.conn = None

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(self.connect_str)
            self.conn.autocommit = True
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
        else:
            Databases.create_table(self.table_name)
        return self

    def run_sql_command(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    @staticmethod
    def run(command_list):
        process = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        error = process.stderr.decode("utf-8")
        if len(error) > 0:
            return error
        return process.stdout.decode("utf-8")

    @staticmethod
    def create_table(filename):
        return Databases.run(['psql', '-f', filename])
