from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

Builder.load_string(
"""
<BreakFastView>:
    breakfast_grid: breakfast_grid
    ScrollView:
        do_scroll_x: False
        MDGridLayout:
            id: breakfast_grid
            adaptive_height: True
            cols: 2
            padding: '10dp'
            spacing: '10dp'
""")

class BreakFastView(Screen):
    breakfast_grid = ObjectProperty()