#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import stdout

def print_recipe(cookbook, name):
    if name in cookbook:
        stdout.write(f'Recipe for {name}: ')
        print(cookbook[name]['ingredients'])
        print(f'To be eaten for {cookbook[name]["meal"]}.')
        print(f'Take {cookbook[name]["prep_time"]} minute{"s" if (cookbook[name]["prep_time"] != 1) else ""} of cooking.')
    else:
        print(f"Recipe {name} don't exist.")

def print_cookbook(cookbook):
    if (len(cookbook) == 0):
        print(f'Cookbook is empty')
    else:
        for elem in cookbook:
            print_recipe(cookbook, elem)

def delete_recipe(cookbook, name):
    if name in cookbook:
        del cookbook[name]
        print(f'Recipe {name} has been deleted')
    else:
        print(f"Recipe {name} dont't exist.")

def add_recipe(cookbook):
    name = input('enter the recipe name:\n>> ')
    if name in cookbook:
        print(f'{name} already exist')
    else:
        ingredients = input('Enter the ingredients list (n1,n2,n3,...):\n>> ').split(',')
        meal = input('Enter the type of meal:\n>> ')
        while (True):
            try:
                prep_time = int(input('Enter the preparation time in minutes:\n>> '))
                break
            except:
                print('An integer is requered')
        cookbook[name] = {
            'ingredients': ingredients,
            'meal': meal,
            'prep_time': prep_time,
        }
        print(f'{name} has been add to cookbook.')

def init_cookbook():
    cookbook = {
        'sandwich': {
            'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch',
            'prep_time': 10,
        },
        'cake': {
            'ingredients': ['flour', 'sugar', 'eggs'],
            'meal': 'desert',
            'prep_time': 60,
        },
        'salad': {
            'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
            'meal': 'lunch',
            'prep_time': 15,
        },
    }
    infos = '\nPlease select an option by typing the corresponding number:'
    infos += '\n1: Add a recipe'
    infos += '\n2: Delete a recipe'
    infos += '\n3: Print a recipe'
    infos += '\n4: Print the cookbook'
    infos += '\n5: Quit'
    return (cookbook, infos)

def main():
    cookbook, infos = init_cookbook()
    print(infos)
    while (True):
        try:
            value = input('>> ')
            value = 0 if (value == '') else int(value)
            assert (0 <= value <= 5)
        except:
            print('This option does not exist, please type the corresponding number.')
            print('To exit, enter 5.')
        else:
            print()
            if (value == 1):
                add_recipe(cookbook)
            elif (value == 2):
                if (len(cookbook) == 0):
                    print(f'Cookbook is empty')
                else:
                    print("Please enter the recipe's name to remove:")
                    print(list(cookbook.keys()))
                    name = input('>> ')
                    delete_recipe(cookbook, name)
            elif (value == 3):
                if (len(cookbook) == 0):
                    print(f'Cookbook is empty')
                else:
                    print("Please enter the recipe's name to get its details")
                    print(list(cookbook.keys()))
                    name = input('>> ')
                    print_recipe(cookbook, name)
            elif (value == 4):
                print_cookbook(cookbook)
            elif (value == 5):
                print('Cookbook closed.')
                break
            print(infos)

if __name__ == '__main__':
    main()
