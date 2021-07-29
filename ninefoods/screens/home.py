from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_string(
"""
<HomePage>:
    MDFloatLayout:
        NineBackground:
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            height: '50dp'
            size_hint_y: None
            NineMidText:
                text: 'Recipe'
                padding: ('10dp', '10dp')
            MDIconButton:
                icon: 'magnify'
                on_release: app.change_screen('home', 'search')
        MDBoxLayout:
            orientation: 'vertical'
            ScrollView:
                do_scroll_y: False
                height: '40dp'
                size_hint_y: None
                NineTab:
                    view: view
                    rows: 1
                    adaptive_width: True
                    padding: ('5dp', '0dp')
                    spacing: '5dp'
                    NineTabItem:
                        text: 'Recipes'
                        on_parent: self.parent.select_node(self)
                    NineTabItem:
                        text: 'Breakfast'
                    NineTabItem:
                        text: 'Lunch'
                    NineTabItem:
                        text: 'Dinner'
            ScreenManager:
                id: view
                AllRecipeView:
                    name: 'recipes'
                BreakFastView:
                    name: 'breakfast'
                LunchView:
                    name: 'lunch'
                DinnerView:
                    name: 'dinner'
""")


class HomePage(Screen):
    pass