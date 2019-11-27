#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.ui.ChoiceScreen import ChoiceScreen
from src.ui.WorkerScreen import WorkerScreen


class MainApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(ChoiceScreen(name="choice"))
        sm.add_widget(WorkerScreen(name="worker"))
        sm.current = "choice"

        return sm


if __name__ == '__main__':
    MainApp().run()
