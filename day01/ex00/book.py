from datetime import datetime
from recipe import Recipe

def get_actual_time():
    now = datetime.now()
    return(f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}')

class Book():
    def __init__(self):
        while (True):
            self.name = input('Enter the cookbook name:\n>> ')
            try: assert(self.name)
            except: print('Cookbook name must not be empty.')
            else: break
        now = get_actual_time()
        self.last_update = now
        self.creation_date = now
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': [],
        }
    def update_time(self):
        self.last_update = get_actual_time()
    def get_recipe_by_name(self, name):
        for elem in self.recipes_list:
            for recipe in self.recipes_list[elem]:
                if (recipe.name == name):
                    print(str(recipe))
                    return (recipe)
        print(f'There is no recipe {name}')
    def get_recipe_by_type(self, recipe_type):
        try: self.recipes_list[recipe_type]
        except: print(f'{recipe_type} don\'t exist.')
        else:
            if (not len(self.recipes_list[recipe_type])):
                print(f'There are not {recipe_type} recipe.')
            else:
                for elem in self.recipes_list[recipe_type]:
                    print(elem.name)
    def add_recipe(self, recipe):
        try: assert(type(recipe) == Recipe)
        except: print(f'error: add_recipe param is {type(recipe)} it must be an instance of Recipe')
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.update_time()
