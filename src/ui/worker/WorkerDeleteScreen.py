#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.Workers import WorkersDB
from data.const import PATH_DB


Builder.load_file('./kv/workerdelete.kv')


class WorkerDeleteScreen(Screen):

    def worker_delete_fun(self):

        input_id = self.worker_delete_input_id.text
        wdb = WorkersDB(PATH_DB)
        wdb.create()
        wdb.remove(input_id)
