from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_string(
"""
<SearchScreen>:
    MDFloatLayout:
        NineBackground:
        MDBoxLayout:
            orientation: 'vertical'
            padding: '5dp'
            spacing: '10dp'
            MDBoxLayout:
                height: '40dp'
                size_hint_y: None
                MDIconButton:
                    icon: 'chevron-left'
                    on_release: app.change_screen('', 'home')
                NineMidText:
                    text: 'Search'
                    padding: ('10dp', '10dp')

            MDCard:
                height: search_field.height + dp(10)
                size_hint_y: None
                padding: '5dp'
                radius: '20dp'
                MDIcon:
                    icon: 'magnify'
                    size_hint: None, None
                    size: '25dp', '25dp'
                    font_size: '18sp'
                    halign: 'center'
                    pos_hint: {'center_y':.5}
                TextInput:
                    id: search_field
                    hint_text: 'Search Recipe'
                    height: '30dp'
                    background_color: [0, 0, 0, 0]
                    on_text: app.search(self.text, search_list)
            ScrollView:
                MDBoxLayout:
                    id: search_list
                    adaptive_height: True
                    orientation: 'vertical'
                    spacing: '5dp'
""")
class SearchScreen(Screen):
    pass
