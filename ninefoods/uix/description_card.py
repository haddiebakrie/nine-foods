from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

Builder.load_string(
"""
<NineDescriptionCard>:
    size_hint_y: None
    padding: '10dp'
    height: desc.height + dp(20)
    spacing: '5dp'
    MDIcon:
        icon: 'circle-medium'
        pos_hint: {'top':1}
        size_hint: None, None
        size: '18dp', '18dp'
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
    MDLabel:
        id: desc
        text: root.text
        height: self.texture_size[1]
        size_hint_y: None
"""

)


class NineDescriptionCard(MDCard):
    text = StringProperty()