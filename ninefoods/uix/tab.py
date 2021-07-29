from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.behaviors import ButtonBehavior, CompoundSelectionBehavior, FocusBehavior
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_string(
"""
<NineTab>:
    app: app
    height: '40dp'
    size_hint_y: None

<NineTabItem>:
    rows: 2
    text: ''
    size_hint_x: None
    # adaptive_height: True
    icon: ''
    text_color: app.gray
    MDLabel:
        text: root.text
        bold: True
        halign:'center'
        theme_text_color: 'Custom'
        text_color: root.text_color
        font_size: '15sp'
    MDIcon: 
        theme_text_color: 'Custom'
        halign:'center'
        icon: root.icon
        font_size: '12sp'
        text_color: root.text_color
"""
)

class NineTabItem(MDGridLayout):
    pass

class NineTab(FocusBehavior, CompoundSelectionBehavior, MDGridLayout):
    '''A navigation panel for the main window.'''
    row = 1
    app = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_widget(self, widget):
        widget.bind(
            on_touch_down=self.button_touch_down,
        )
        return super(NineTab, self).add_widget(widget)

    def select_node(self, node):
        node.icon = 'circle-medium'
        node.text_color= self.app.theme_cls.primary_color
        self.view.current = node.text.lower()
        return super(NineTab, self).select_node(node)

    def deselect_node(self, node):
        node.icon = ''
        node.text_color= self.app.gray
        return super(NineTab, self).deselect_node(node)

    def button_touch_down(self, button, touch):
        if button.collide_point(*touch.pos):
            self.select_with_touch(button, touch)