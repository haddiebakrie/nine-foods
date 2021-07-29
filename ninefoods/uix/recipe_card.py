from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder

Builder.load_string(

"""
<RecipeCard>:
    source: ''
    size_hint_y: None
    height: '200dp'
    radius: ('20dp', )
    elevation: 12
    cuisine: ''
    food_name: ''
    orientation: 'vertical'
    padding: ('5dp', '5dp')
    spacing: '15dp'
    time: ''
    on_release: app.load_detail(self.food_name, 'home')
    MDFloatLayout:
        FitImage:
            source: root.source
            radius: root.radius
            pos_hint: {'center_x':.5, 'center_y':.5}

    MDBoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        adaptive_height: True
        NineSmallText:
            text: root.food_name
            shorten_from: 'right'
            shorten: True
            padding: ('8dp', '0dp')
            bold: True
        NineSmallText:
            text: root.cuisine
            padding: ('8dp', '2dp')
            color: app.gray
"""
)

class RecipeCard(MDCard):
    pass