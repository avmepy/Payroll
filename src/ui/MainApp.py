#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.ui.ChoiceScreen import ChoiceScreen
from src.ui.worker.WorkerMainScreen import WorkerMainScreen
from src.ui.worker.WorkerAddScreen import WorkerAddScreen
from src.ui.worker.WorkerChangeScreen import WorkerChangeScreen
from src.ui.worker.WorkerDeleteScreen import WorkerDeleteScreen
from src.ui.position.PositionMainScreen import PositionMainScreen
from src.ui.position.PositionAddScreen import PositionAddScreen
from src.ui.position.PositionChangeScreen import PositionChangeScreen
from src.ui.position.PositionDeleteScreen import PositionDeleteScreen


class MainApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(ChoiceScreen(name="choice"))
        sm.add_widget(WorkerMainScreen(name="workermain"))
        sm.add_widget(WorkerAddScreen(name="workeradd"))
        sm.add_widget(WorkerChangeScreen(name="workerchange"))
        sm.add_widget(WorkerDeleteScreen(name="workerdelete"))
        sm.add_widget(PositionMainScreen(name="positionmain"))
        sm.add_widget(PositionAddScreen(name="positionadd"))
        sm.add_widget(PositionChangeScreen(name="positionchange"))
        sm.add_widget(PositionDeleteScreen(name="positiondelete"))
        sm.current = "choice"

        return sm


if __name__ == '__main__':
    MainApp().run()
