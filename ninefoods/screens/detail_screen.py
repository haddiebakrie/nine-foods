from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty

Builder.load_string( 
"""
<DetailScreen>:
    swiper: swiper
    md_bg_color: [1, 1, 1, 1]
    MDBoxLayout:
        md_bg_color: [1, 1, 1, 1]
        MDFloatLayout:
            MDSwiper:
                id: swiper
                size_hint_y: None
                height: root.height/2 - dp(40)
                pos_hint: {'top':1}
                items_spacing: '5dp'
                md_bg_color: [1, 1, 1, 1]
            MDBoxLayout:
                height: '60dp'
                size_hint_y: None
                padding: ('5dp', '5dp')
                pos_hint: {'top':1}
                MDIconButton:
                    icon: 'chevron-left'
                    on_press: app.change_screen(root.back, root.back)
                    md_bg_color: app.theme_cls.primary_color
                    user_font_size: '20sp'
                    theme_text_color: 'Custom'
                    text_color: [1, 1, 1, 1]

            MDCard:
                height: root.height/2 + dp(40)
                size_hint_y: None
                orientation: 'vertical'
                padding: '10dp'
                elevation: 0
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    adaptive_height: True
                    padding: '5dp'
                    spacing: '5dp'
                    NineBigText:
                        id: food
                        text: root.food
                        halign: 'center'
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: '10dp'
                    MDGridLayout:
                        cols: 2
                        spacing: '10dp'
                        TwoLineIconList:
                            icon: 'timelapse'
                            text: root.time
                            secondary_text: 'Cooking Time'
                        TwoLineIconList:
                            icon: 'emoticon-tongue-outline'
                            text: root.difficulty
                            secondary_text: 'Difficulty'
                        TwoLineIconList:
                            icon: 'playlist-check'
                            text: root.ingredients_len
                            secondary_text: 'Ingredients'
                        TwoLineIconList:
                            icon: 'room-service'
                            text: root.serving
                            secondary_text: 'Serving'
                    
                    MDFillRoundFlatButton:
                        text: 'Start Cooking'
                        pos_hint: {'center_x': .5}
                        on_release: app.load_recipe(root.food, root.back)
                        size_hint_x: 1
                        halign: 'center'
""")

class DetailScreen(Screen):
    image = StringProperty()
    food = StringProperty()
    cuisine = StringProperty()
    back = StringProperty()
    ingredients_len = StringProperty()
    serving = StringProperty()
    difficulty = StringProperty()
    time = StringProperty()
    swiper = ObjectProperty()
