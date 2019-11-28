#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


import sqlite3
import pickle
import re


class StatementDB:

    def __init__(self, filename):
        self.filename = filename

    def create(self):

        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS statement (id_statement INT, id_worker INT, cmonth TEXT, amount BLOB)")
        conn.commit()
        conn.close()

    def append(self, id_statement, id_worker, cmonth, amount):

        patt = re.compile(r'\s')
        d = {}
        for i, j in enumerate(patt.split(amount)):
            d[i+1] = j

        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO statement VALUES (?, ?, ?, ?)",
                     (id_statement, id_worker, cmonth, pickle.dumps(d)))
        conn.commit()
        conn.close()

    def find(self, id_statement):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT * FROM statement WHERE id = ?", (id_statement,))
        res = curs.fetchall()
        conn.commit()
        conn.close()
        return res

    def find_pay(self, id_worker, cmonth):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT id_statement FROM statement WHERE id_worker = ? AND month = ?", (id_worker, cmonth))

    def change(self, id_statement, id_worker, cmonth, amount):
        patt = re.compile(r'\s')
        d = {}
        for i, j in enumerate(patt.split(amount)):
            d[i + 1] = j
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("UPDATE statement SET id_worker = ? , cmonth = ?, amount = ? WHERE id_statement = ?",
                     (id_worker, cmonth, pickle.dumps(d), id_statement))
        conn.commit()
        conn.close()

    def remove(self, id_statement):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("DELETE FROM statement WHERE id_statement = ?", (id_statement, ))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    sdb = StatementDB("../data/data.db")
    sdb.create()
    sdb.append(301, 201, "Січень", "4 5 4 4 4 5 3 4 4 5 5 5 4 л 4 2 5 6 8 5 3 4 4 5 5 5 4 4 4 5")
