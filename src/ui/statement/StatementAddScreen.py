#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from data.const import PATH_DB, MONTHS
from src.Positions import PositionsDB


Builder.load_file('./kv/statementadd.kv')


class StatementAddScreen(Screen):

    def position_add_fun(self):
        input_id = self.position_add_input_id.text
        input_name = self.position_add_input_name.text
        input_salary = self.position_add_input_salary.text
        pdb = PositionsDB(PATH_DB)
        pdb.create()
        pdb.append(input_id, input_name, input_salary)

