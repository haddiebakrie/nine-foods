from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty

class BreakFastView(Screen):
    breakfast_grid = ObjectProperty()

class LunchView(Screen):
    pass

class DinnerView(Screen):
    pass

class PopularView(Screen):
    pass