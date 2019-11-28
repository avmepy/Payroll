#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.Statement import StatementDB
from data.const import PATH_DB


Builder.load_file('./kv/statementadd.kv')


class StatementAddScreen(Screen):

    def statement_add_fun(self):

        input_id_statement = self.statement_add_input_id_statement.text
        input_id_worker = self.statement_add_input_id_worker.text
        input_cmonth = self.statement_add_input_cmonth.text
        input_hours = self.statement_add_input_amount.text

        sdb = StatementDB(PATH_DB)
        sdb.create()
        sdb.append(input_id_statement, input_id_worker, input_cmonth, input_hours)
