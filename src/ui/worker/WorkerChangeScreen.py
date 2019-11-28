#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.Workers import WorkersDB
from data.const import PATH_DB


Builder.load_file('./kv/workerchange.kv')


class WorkerChangeScreen(Screen):

    def worker_change_fun(self):
        input_id = self.worker_change_input_id.text
        input_name = self.worker_change_input_name.text
        input_position = self.worker_change_input_position.text

        wdb = WorkersDB(PATH_DB)
        wdb.create()
        wdb.change(input_id, input_name, input_position)
