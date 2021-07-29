from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ListProperty, StringProperty

Builder.load_string(
"""
<RecipeScreen>:
    MDBoxLayout:
        MDFloatLayout:
            FitImage:
                source: root.image
                size_hint_y: None
                height: root.height/2
                pos_hint: {'top':1}
            MDBoxLayout:
                height: '60dp'
                size_hint_y: None
                padding: ('5dp', '5dp')
                pos_hint: {'top':1}
                MDIconButton:
                    icon: 'chevron-left'
                    # padding: ('10dp', '10dp')
                    on_press: app.change_screen(root.back, root.back)
                    md_bg_color: app.theme_cls.primary_color
                    user_font_size: '20sp'
                    theme_text_color: 'Custom'
                    text_color: [1, 1, 1, 1]
            
            MDCard:
                height: root.height - dp(100)
                size_hint_y: None
                radius: ('20dp', )
                orientation: 'vertical'
                padding: '10dp'
                spacing: '10dp'
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    adaptive_height: True
                    padding: '5dp'
                    spacing: '5dp'
                    NineMidText:
                        id: food
                        text: root.food
                        halign: 'center'
                    NineSmallText:
                        id: cuisine
                        text: root.cuisine
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.gray
                MDBoxLayout:
                    size_hint_y: None
                    height: '80dp'
                    padding: '5dp'
                    orientation: 'vertical'
                    MDBoxLayout:
                        pos_hint: {'center_x':.5}
                        adaptive_size: True
                        spacing: '10dp'
                        NineIconLabel:
                            icon: root.time_icon
                            text: root.time
                        NineIconLabel:
                            icon: root.serving_icon
                            text: root.serving
                        NineIconLabel:
                            icon: root.diff_icon
                            text: root.difficulty
                MDBoxLayout:
                    orientation: 'vertical'
                    NineTab:
                        view: view
                        rows: 1
                        padding: ('5dp', '0dp')
                        NineTabItem:
                            text: 'Ingredient'
                            on_parent: self.parent.select_node(self)
                            height: '30dp'
                            size_hint_y: None
                            size_hint_x: 1
                        NineTabItem:
                            text: 'Direction'
                            height: '30dp'
                            size_hint_y: None
                            size_hint_x: 1
                    ScreenManager:
                        id: view
                        IngredientList:
                            id: ingredients
                            name: 'ingredient'

                        DirectionList:
                            name: 'direction'
                            id: directions
                            
""")

class RecipeScreen(Screen):

    image = StringProperty()
    food = StringProperty()
    cuisine = StringProperty()
    diff_icon = StringProperty('layers')
    time = StringProperty()
    time_icon = StringProperty('clock')
    serving_icon = StringProperty('room-service')
    serving = StringProperty()
    ingredient = ListProperty()
    direction = ListProperty()
    difficulty = StringProperty()
    back = StringProperty()
    description = StringProperty()