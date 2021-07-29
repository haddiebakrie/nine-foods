from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

Builder.load_string(
"""<LunchView>:
    lunch_grid: lunch_grid
    ScrollView:
        do_scroll_x: False
        MDGridLayout:
            id: lunch_grid
            adaptive_height: True
            cols: 2
            padding: '10dp'
            spacing: '10dp'
""")


class LunchView(Screen):
    lunch_grid = ObjectProperty()
