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
        curs.execute("""CREATE TABLE IF NOT EXISTS 
                     positions (position_id INT, position_name TEXT, salary_ph INT, number_hours INT)""")
        conn.commit()
        conn.close()

    def append(self, position_id, position_name, salary_ph, number_hours):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO positions VALUES (?, ?, ?, ?)", (position_id, position_name, salary_ph, number_hours))
        conn.commit()
        conn.close()

    def find(self, position_id):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT * FROM positions WHERE position_id = ?", (position_id,))
        res = curs.fetchall()
        conn.commit()
        conn.close()
        return res

    def change(self, position_id, position_name, salary_ph, number_hours):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("UPDATE positions SET position_name = ?, salary_ph = ?, number_hours = ? WHERE position_id = ?",
                     (position_name, salary_ph, number_hours, position_id))
        conn.commit()
        conn.close()

    def remove(self, position_id):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("DELETE FROM  positions WHERE position_id = ?", (position_id,))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    pdb = PositionsDB("../data/data.db")
    pdb.create()
