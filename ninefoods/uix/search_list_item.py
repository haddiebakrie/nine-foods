from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

Builder.load_string(
"""
<NineSearchList>:
    size_hint_y: None
    height: '70dp'
    adaptive_height: True
    padding: '5dp'
    spacing: '5dp'
    on_release: app.load_recipe(self.text, 'search')
    FitImage:
        source: root.image
        size_hint: None, None
        size: '60dp', '60dp'
        radius: 10, 
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '3dp'
        MDLabel:
            text: root.text
            bold: True
            shorten: True
            shorten_from: 'right'
        MDLabel:
            text: root.description
            shorten: True
            shorten_from: 'right'
        MDLabel:
            text: root.cuisine

""")

class NineSearchList(MDCard):
    image = StringProperty()
    text = StringProperty()
    cuisine = StringProperty()
    description = StringProperty()