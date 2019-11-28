#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.Positions import PositionsDB
from data.const import PATH_DB


Builder.load_file('./kv/positiondelete.kv')


class PositionDeleteScreen(Screen):

    def position_delete_fun(self):

        input_id = self.position_delete_input_id.text

        pdb = PositionsDB(PATH_DB)
        pdb.create()
        pdb.remove(input_id)
