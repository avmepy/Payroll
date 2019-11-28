#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.Positions import PositionsDB
from data.const import PATH_DB


Builder.load_file('./kv/positionchange.kv')


class PositionChangeScreen(Screen):

    def position_change_fun(self):
        input_id = self.position_change_input_id.text
        input_name = self.position_change_input_name.text
        input_salary = self.position_change_input_salary.text
        input_hours = self.position_change_input_hours.text

        pdb = PositionsDB(PATH_DB)
        pdb.create()
        pdb.change(input_id, input_name, input_salary, input_hours)