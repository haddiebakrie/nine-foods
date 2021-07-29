from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder

Builder.load_string(
    """ 
<AllRecipeView>:
    all_recipe_grid: all_recipe_grid
    ScrollView:
        do_scroll_x: False
        MDGridLayout:
            id: all_recipe_grid
            adaptive_height: True
            cols: 2
            padding: '10dp'
            spacing: '10dp'
""")

class AllRecipeView(Screen):
    pass