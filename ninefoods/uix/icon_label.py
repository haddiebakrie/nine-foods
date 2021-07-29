from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.properties import StringProperty


Builder.load_string(
"""
<NineIconLabel>:
    orientation: 'vertical'
    size_hint: None, None
    size: ('60dp', '70dp')
    md_bg_color: app.theme_cls.primary_color
    radius: '15dp'
    padding: '5dp'
    adaptive_width: True
    spacing: '5dp'
    MDIcon:
        icon: root.icon
        halign: 'center'
        font_size: '20sp'
        md_bg_color: [1, 1, 1, 1]
        radius: '10dp'
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
    NineXSmallText:
        text: root.text
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: [1, 1, 1, 1]
        bold: True
""")

class NineIconLabel(MDCard):
    icon = StringProperty()
    text = StringProperty()