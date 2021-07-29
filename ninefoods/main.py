import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import RiseInTransition, Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.core.window import Window

# My Imports....
from screens.screens import *
from chef.chef import Chef

from uix.uix import *

class NineFoods(MDApp):
    '''Root of the Application.
    '''
    def build(self):
        # Theming #############
        self.theme_cls.primary_palette = 'Red'
        # self.theme_cls.theme_style = 'Dark'
        self.gray = [.4, .4, .4, 1]
        # End Theming #############

        self.bg = 'chef/food_imgs/backdrop-01.jpg'
        self.prev = ''

        self.route = WindowManager(transition=RiseInTransition())
        screens = [
            LandingScreen(name='landing'),
            HomePage(name='home'),
            SearchScreen(name='search'),

        ]
        for screen in screens:
            self.route.add_widget(screen)

        Window.bind(on_keyboard=self.hook_keyboard)
        self.murphy = Chef('chef/nine_foods.json')

        return self.route

    def change_screen(self, current, screen):
        if self.prev == 'home':
            self.prev = ''
        self.prev = current
        self.route.current = screen


    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            if self.route.current == 'home':
                self.stop()
                return True
            if self.prev != '':
                self.route.current = self.prev
                return True


    def load_home(self):
        self.load_all_recipe()
        view = self.route.screens[1].ids['view']
        self.murphy = Chef('chef/nine_foods.json')
        food_names = self.murphy.get_food_names()
        for food_name in food_names:
            recipe_card = RecipeCard()
            food_image = self.murphy.get_image(food_name)
            food_cuisine = self.murphy.get_cuisine(food_name)
            food_time = self.murphy.get_total_time(food_name)
            food_serving = self.murphy.get_serving(food_name)
            food_difficulty = self.murphy.get_difficulty(food_name)
            food_tag = self.murphy.get_tag(food_name)
            recipe_card.food_name = food_name
            recipe_card.cuisine = food_cuisine
            recipe_card.time = food_time
            recipe_card.serving = food_serving
            recipe_card.tag = food_tag
            recipe_card.difficulty = food_difficulty.title()
            recipe_card.source = f'chef/food_imgs/{food_image[0]}'
            if recipe_card.tag == 'Breakfast':
                view.screens[1].ids['breakfast_grid'].add_widget(recipe_card)
            elif recipe_card.tag == 'Lunch':
                view.screens[2].ids['lunch_grid'].add_widget(recipe_card)
            elif recipe_card.tag == 'Dinner':
                view.screens[3].ids['dinner_grid'].add_widget(recipe_card)

        self.route.current = 'home'
        self.prev = ''

    def load_all_recipe(self):
        view = self.route.screens[1].ids['view']
        self.murphy = Chef('chef/nine_foods.json')
        food_names = self.murphy.get_food_names()
        for food_name in food_names:
            recipe_card = RecipeCard()
            food_image = self.murphy.get_image(food_name)
            food_cuisine = self.murphy.get_cuisine(food_name)
            food_time = self.murphy.get_total_time(food_name)
            food_serving = self.murphy.get_serving(food_name)
            food_difficulty = self.murphy.get_difficulty(food_name)
            food_tag = self.murphy.get_tag(food_name)
            recipe_card.food_name = food_name
            recipe_card.cuisine = food_cuisine
            recipe_card.time = food_time
            recipe_card.serving = food_serving
            recipe_card.tag = food_tag
            recipe_card.difficulty = food_difficulty.title()
            recipe_card.source = f'chef/food_imgs/{food_image[0]}'
            view.screens[0].ids['all_recipe_grid'].add_widget(recipe_card)

    def load_recipe(self, food, back):
        recipe_page = RecipeScreen()
        recipe_page.food = food
        recipe_page.image = f'chef/food_imgs/{self.murphy.get_image(food)[0]}'
        recipe_page.time = self.murphy.get_total_time(food)
        recipe_page.serving = self.murphy.get_serving(food)
        recipe_page.difficulty = self.murphy.get_difficulty(food)
        recipe_page.cuisine = self.murphy.get_cuisine(food)
        recipe_page.back = back
        ingredients_list = recipe_page.ids['ingredients']
        directions_list = recipe_page.ids['directions']
        # self.route.add_widget = RecipePage(name='recipe')
        for ingredients in self.murphy.get_ingredients(food):
            ingredients_name, ingredients_quantity =  ingredients['name'], ingredients['quantity']
            list_item = NineListItem()
            list_item.text = ingredients_name
            list_item.secondary_text = ingredients_quantity
            ingredients_list.ingredient_list.add_widget(list_item)

        for direction in self.murphy.get_direction(food):
            direction_item = NineDescriptionCard()
            direction_item.text = direction
            directions_list.direction_list.add_widget(direction_item)
        self.prev = back
        self.route.switch_to(recipe_page)

    def search(self, word, list_layout):
        results = self.murphy.search_with_keyword(word)
        list_layout.clear_widgets()
        for result in results:
            search_list = NineSearchList()
            search_list.text = result
            search_list.description = self.murphy.get_description(result)
            images = self.murphy.get_image(result)
            search_list.image = f'chef/food_imgs/{images[0]}'
            search_list.cuisine = self.murphy.get_cuisine(result)
            list_layout.add_widget(search_list)

    def load_detail(self, food, back):
        detail_page = DetailScreen()
        detail_page.food = food
        detail_page.back = back
        detail_page.cuisine = self.murphy.get_cuisine(food)
        detail_page.description = self.murphy.get_description(food)
        ingredients = self.murphy.get_ingredients(food)
        detail_page.serving = self.murphy.get_serving(food)
        detail_page.ingredients_len = str(len(ingredients))
        detail_page.difficulty = self.murphy.get_difficulty(food).title()
        detail_page.time = self.murphy.get_total_time(food)
        for image in self.murphy.get_image(food):
            swipe_card = SwipeImage()
            swipe_card.source = f'chef/food_imgs/{image}'
            detail_page.swiper.add_widget(swipe_card)
            
        self.route.switch_to(detail_page)

        

if __name__ == '__main__':
    NineFoods().run()

