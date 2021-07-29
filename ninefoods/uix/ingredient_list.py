from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_string(

"""
<IngredientList>:
    ingredient_list: ingredient_list
    MDBoxLayout:
        ScrollView:
            do_scroll_x: False
            scroll_effects: 'ScrollView'
            MDBoxLayout:
                id: ingredient_list
                radius: '20dp'
                orientation: 'vertical'
                spacing: '2dp'
                padding: '2dp'
                adaptive_height: True
"""
)

class IngredientList(Screen):
    pass