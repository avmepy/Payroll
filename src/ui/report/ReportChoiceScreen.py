#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.filechooser import FileChooserListView


Builder.load_file('./kv/reportchoice.kv')


class ReportChoiceScreen(Screen):

    def get_report_worker(self):
        pass

    def get_report_position(self):
        pass

    def get_report_pay(self):
        pass
