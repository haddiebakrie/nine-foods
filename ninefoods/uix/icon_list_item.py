from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

Builder.load_string(

"""
<TwoLineIconList>:
    height: '58dp'
    size_hint_y: None
    md_bg_color: app.theme_cls.primary_color
    padding: dp(1), 
    radius: dp(5), dp(5)
    icon: ''
    MDCard:
        size_hint_y: None
        height: '56dp'
        spacing: dp(5)
        padding: dp(5)
        radius: dp(5), dp(5)
        elevation: 0
        pos_hint: {'center_x':.5, 'center_y':.5}
        MDIcon:
            icon: root.icon
            size_hint: None, None
            size:  self.texture_size
            pos_hint: {'center_y':.5}
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '5dp'
            padding: dp(5)
            MDLabel:
                text: root.text
                font_size: '15sp'
                bold: True
                height: self.texture_size[1]
                size_hint_y: None
                shorten_from: 'right'
                shorten: True
                theme_text_color: 'Custom'
                text_color: app.theme_cls.primary_color
            MDLabel:
                text: root.secondary_text
                font_size: '12sp'
                height: self.texture_size[1]
                size_hint_y: None
                shorten_from: 'right'
                shorten: True
"""
)

class TwoLineIconList(MDBoxLayout):
    text = StringProperty()
    secondary_text = StringProperty()
    icon = StringProperty()