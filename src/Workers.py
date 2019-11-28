#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

import sqlite3
from data.const import PATH_DB


class WorkersDB:

    def __init__(self, filename):
        self.filename = filename

    def create(self):

        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS workers (worker_id INT, name TEXT, position TEXT)")
        conn.commit()
        conn.close()

    def append(self, worker_id, name, position):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO workers VALUES (?, ?, ?)", (worker_id, name, position))
        conn.commit()
        conn.close()

    def find(self, worker_id):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT * FROM workers WHERE worker_id = ?", (worker_id,))
        res = curs.fetchall()
        conn.commit()
        conn.close()
        return res

    def change(self, worker_id, name, position):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("UPDATE workers SET name = ? , position = ? WHERE worker_id = ?", (name, position, worker_id))
        conn.commit()
        conn.close()

    def remove(self, worker_id):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("DELETE FROM  workers WHERE worker_id = ?", (worker_id, ))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    wdb = WorkersDB(PATH_DB)
    wdb.create()

