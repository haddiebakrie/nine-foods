import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import RiseInTransition, Screen, ScreenManager
from kivy.lang.builder import Builder

# My Imports....
from uix.screens import (
    WindowManager, 
    LandingPage, 
    HomePage,
    )
from uix.cards import RecipeCard
from chef.chef import Chef

from uix.tab import NineTabItem
from uix.views import BreakFastView, LunchView, DinnerView, PopularView

Builder.load_file('pages/home.kv')


class NineFoods(MDApp):
    '''Root of the Application.
    '''

    def build(self):
        # Theming #############
        self.theme_cls.primary_palette = 'Red'
        self.gray = [.4, .4, .4, 1]
        # End Theming #############

        self.route = WindowManager(transition=RiseInTransition())
        screens = [
            LandingPage(name='landing'),
            HomePage(name='home'),

        ]
        for screen in screens:
            self.route.add_widget(screen)

        self.load_breakfast()

        return self.route

    def change_screen(self, screen):
        self.route.current = screen

    def load_breakfast(self):
        view = self.route.screens[1].ids['view'].screens[0]
        self.murphy = Chef('chef/nine_foods.json')
        food_names = self.murphy.get_food_names()
        for food_name in food_names:
            recipe_card = RecipeCard()
            food_image = self.murphy.get_image(food_name)
            food_cuisine = self.murphy.get_cuisine(food_name)
            food_time = self.murphy.get_total_time(food_name)
            recipe_card.food_name = food_name
            recipe_card.cuisine = food_cuisine
            recipe_card.time = food_time
            recipe_card.source = f'chef/food_imgs/{food_image[0]}'
            view.ids['breakfast_grid'].add_widget(recipe_card)

if __name__ == '__main__':
    NineFoods().run()

