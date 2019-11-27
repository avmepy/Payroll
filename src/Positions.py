#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


import sqlite3


class PositionsDB:

    def __init__(self, filename):
        self.filename = filename

    def create(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS positions (id INT, position_name TEXT, salary_ph INT)")
        conn.commit()
        conn.close()

    def append(self, id, position_name, salary_ph):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO positions VALUES (?, ?, ?)", (id, position_name, salary_ph))
        conn.commit()
        conn.close()

    def find(self, id):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT * FROM positions WHERE id = ?", (id,))
        res = curs.fetchall()
        conn.commit()
        conn.close()
        return res


if __name__ == '__main__':
    pdb = PositionsDB("../data/data.db")
    pdb.create()
