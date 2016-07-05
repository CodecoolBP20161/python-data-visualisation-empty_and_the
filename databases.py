import psycopg2
import subprocess


class Databases:

    def __init__(self, dbname, username, host, password):
        self.dbname = dbname
        self.username = username
        self.host = host
        self.password = password
        self.connect_str = "dbname={0} user={1} host={2} password={3}".format(dbname, username, host, password)
        self.conn = None

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(self.connect_str)
            self.conn.autocommit = True
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)

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