from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

Builder.load_string(
"""
<DinnerView>:
    dinner_grid: dinner_grid
    ScrollView:
        do_scroll_x: False
        MDGridLayout:
            id: dinner_grid
            adaptive_height: True
            cols: 2
            padding: '10dp'
            spacing: '10dp'

""")

class DinnerView(Screen):
    dinner_grid = ObjectProperty()


