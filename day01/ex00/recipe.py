class Recipe:
    def __init__(self):
        while (True):
            self.name = input('Enter recipe name:\n>> ')
            try: assert (self.name)
            except: print('name must not be empty.')
            else: break
        while (True):
            try:
                self.cooking_time = int(input('Enter cooking time:\n>> '))
                assert (self.cooking_time >= 0)
            except: print('Cooking time must be a positive integer.')
            else: break
        while (True):
            self.ingredients = input('Enter ingredients list (n1,n2,n3,...):\n>> ').split(',')
            i = 0
            while (i < len(self.ingredients)):
                self.ingredients[i] = self.ingredients[i].strip()
                if (not self.ingredients[i]): del self.ingredients[i]
                else: i += 1
            try: assert (len(self.ingredients))
            except: print('Ingredients list must not be empty.')
            else: break
        self.description = input('Enter a description of the recipe:\n>> ')
        while (True):
            self.recipe_type = input('Enter the recipe type (starter, lunch or dessert):\n>> ')
            try: assert (self.recipe_type)
            except: print('Repice type must not be empty.')
            else:
                try: assert (self.recipe_type == 'starter' or self.recipe_type == 'lunch' or self.recipe_type == 'dessert')
                except: print('Recipe type must be \'starter\' or \'lunch\' or \'dessert\', nothing else.')
                else: break
    def __str__(self):
        recipe_info = ''
        recipe_info += f'Name = {self.name}\n'
        recipe_info += f'Cooking_time = {self.cooking_time}\n'
        recipe_info += f'Ingredients = {self.ingredients}\n'
        recipe_info += f'Description = {self.description}\n'
        recipe_info += f'Recipe_type = {self.recipe_type}'
        return (recipe_info)
