#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

import sqlite3


class ReportCartDB:

    def __init__(self, filename):
        self.filename = filename

    def create(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS reports (id_statement INT, id_worker INT, month TEXT, amount INT)")
        conn.commit()
        conn.close()

    def append(self, id_statement, id_worker, month, amount):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO reports VALUES (?, ?, ?, ?)", (id_statement, id_worker, month, amount))
        conn.commit()
        conn.close()

    def find(self, id_statement):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT * FROM reports WHERE id_statement = ?", (id_statement,))
        res = curs.fetchall()
        conn.commit()
        conn.close()
        return res

    def find_pay(self, id_worker, month):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT id_statement FROM reports WHERE id_worker = ? AND month = ?", (id_worker, month))


if __name__ == '__main__':
    rcdb = ReportCartDB("../data/data.db")
    rcdb.create()