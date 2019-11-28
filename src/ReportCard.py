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
        curs.execute("CREATE TABLE IF NOT EXISTS reports (id_report INT, id_worker INT, cmonth TEXT, amount INT)")
        conn.commit()
        conn.close()

    def append(self, id_report, id_worker, cmonth, amount):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO reports VALUES (?, ?, ?, ?)", (id_report, id_worker, cmonth, amount))
        conn.commit()
        conn.close()

    def find(self, id_report):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT * FROM reports WHERE id_report = ?", (id_report,))
        res = curs.fetchall()
        conn.commit()
        conn.close()
        return res

    def find_pay(self, id_worker, cmonth):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT id_report, amount FROM reports WHERE id_worker = ? AND cmonth = ?", (id_worker, cmonth))


if __name__ == '__main__':
    rdb = ReportCartDB("../data/data.db")
    rdb.create()
