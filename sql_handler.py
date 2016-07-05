import psycopg2


class DBconnection:

    def __init__(self, dbname, username, host, password):
        self.dbname = dbname
        self.username = username
        self.host = host
        self.password = password
        self.connect_str = "dbname={0} user={1} host={2} password={3}".format(dbname, username, host, password)
        self.conn = None

    def connect_sql(self):
        try:
            self.conn = psycopg2.connect(self.connect_str)
            self.conn.autocommit = True
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)

    def run_sql(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
