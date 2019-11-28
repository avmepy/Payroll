#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.Workers import WorkersDB
from data.const import PATH_DB


Builder.load_file('./kv/workeradd.kv')


class WorkerAddScreen(Screen):

    def worker_add_fun(self):
        worker_id = self.worker_add_input_id.text
        worker_name = self.worker_add_input_name.text
        worker_position = self.worker_add_input_position.text
        wdb = WorkersDB(PATH_DB)
        wdb.create()
        wdb.append(worker_id, worker_name, worker_position)
        print(worker_id, worker_name, worker_position)

