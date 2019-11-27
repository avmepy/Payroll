#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

import sqlite3


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


if __name__ == '__main__':
    wdb = WorkersDB("../data/data.db")
    wdb.create()
