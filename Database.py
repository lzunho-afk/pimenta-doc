# -*- Coding: utf-8 -*-

import psycopg2

class Database:
    def __init__(self, config):
        self.config = config
        self.get_connection()

    def get_connection(self):
        ''' Create a database connection & print Postgresql version '''
        try:
            # Start server connection
            self.db_conn = psycopg2.connect(
                    dbname=self.config['database'],
                    user=self.config['user'],
                    password=self.config['password'],
                    host=self.config['host'],
                    port=self.config['port'])

            # Print postgresql version
            db_cur = self.db_conn.cursor()
            db_cur.execute('SELECT version()')
            print("[*] Connected with postgresql {\n\tVersion: {}\n}".format(db_cur.fetchone()))
            db_cur.close()
        except (Exception, psycopg2.DatabaseError) as e:
            sys.exit(e)
