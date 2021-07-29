from kivymd.uix.swiper import MDSwiperItem
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_string(

"""
<SwipeImage>:
    padding: '10dp'
    FitImage:
        source: root.source
        radius: dp(30),
"""
)

class SwipeImage(MDSwiperItem):
    source = ObjectProperty()