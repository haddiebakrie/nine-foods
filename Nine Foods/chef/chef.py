import json

class Chef:
    '''A Food Expert'''
    def __init__(self, path_to_json):
        with open(path_to_json) as fb:
            self.foods = json.load(fb)

    def get_food_names(self):
        _food_list = []
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                _food_list.append(_food['name'])
        return _food_list

    def get_cuisine(self, food_name):
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _cuisine = _food['cuisine']
        return _cuisine
    
    def get_prep_time(self, food_name):
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _prep_time = _food['prep_time']
        return _prep_time

    def get_cook_time(self, food_name):
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _cook_time = _food['cook_time']
        return _cook_time
    
    def get_total_time(self, food_name):
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _total_time = _food['total_time']
        return _total_time
    
    def get_description(self, food_name):
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _description = _food['description']
        return _description

    def get_tag(self, food_name):
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _tag = _food['tag']
        return _tag

    def get_image(self, food_name):
        _images = []
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _all_image = _food['images']
                    for _image in _all_image.split(';'):
                        _images.append(_image)
        return _images

    def get_keywords(self, food_name):
        _keywords = []
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    for _keyword in _food['keyword'].split(','):
                        _keywords.append(_keyword.lower())
        return _keywords

    def get_ingredients(self, food_name):
        _ingredients = []
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    for _ingredient in _food['ingredients']:
                        _ingredients.append(_ingredient)
        return _ingredients

    def get_ingredient_names(self, food_name):
        _ingredient_names = []
        _ingredients = self.get_ingredients(food_name)
        for _ingredient in _ingredients:
            _ingredient_name = _ingredient['name']
            _ingredient_names.append(_ingredient_name.lower())
        return _ingredient_names

    def get_ingredient_quantity(self, food_name, ingredient):
        _ingredients = self.get_ingredients(food_name)
        for _ingredient in _ingredients:
            if _ingredient['name'].lower() == ingredient.lower():
                _quantity = _ingredient['quantity']
        return _quantity
    
    def get_direction(self, food_name):
        for _category, _data in self.foods['Nine Foods'].items():
            for _food in _data:
                if _food['name'].lower() == food_name.lower():
                    _direction = _food['direction']
        return _direction

    def search_with_tag(self, tag):
        _result = []
        _food_names = self.get_food_names()
        for _food_name in _food_names:
            _food_tag = self.get_tag(_food_name)
            if tag.lower() in _food_tag.lower():
                _result.append(_food_name)
        return _result

    def search_with_keyword(self, keyword):
        _result = []
        _food_names = self.get_food_names()
        for _food_name in _food_names:
            _food_keywords = self.get_keywords(_food_name)
            for _food_keyword in _food_keywords:
                _raw_food_kw = _food_keyword.strip()
                _food_kw = _raw_food_kw.split(' ')
                for _kw in keyword.split(' '):
                    if _kw in _food_kw:
                        if _food_name not in _result:
                            _result.append(_food_name)
        return _result

    def search_with_ingredient(self, ingredient):
        _result = []
        _food_names = self.get_food_names()
        for _food_name in _food_names:
            _food_ingredients = self.get_ingredient_names(_food_name)
            for _food_ingredient in _food_ingredients:
                _raw_food_ing = _food_ingredient.strip()
                _food_ing = _raw_food_ing.split(' ')
                for _ing in ingredient.split(' '):
                    if _ing in _food_ing:
                        if _food_name not in _result:
                            _result.append(_food_name)
        return _result

# murphy = Chef('chef/nine_foods.json')

# img = murphy.get_image('Bread and Egg Toast')
# print(img)