from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

Builder.load_string(
"""
<NineListItem>:
    size_hint_y: None
    height: '40dp'
    padding: '5dp'
    MDLabel:
        text: root.text
    Label:
        text: root.secondary_text
        color: [0, 0, 0, 1]
        width: self.texture_size[0]
        size_hint_x: None
        color: app.theme_cls.primary_color
        bold: True
"""
)


class NineListItem(MDCard):
    text = StringProperty()
    secondary_text = StringProperty()
