#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import stdout

def print_recipe(cookbook, name):
    stdout.write(f'Recipe for {name}: ')
    print(cookbook[name]['ingredients'])
    print(f'To be eaten for {cookbook[name]["meal"]}.')
    print(f'Take {cookbook[name]["prep_time"]} of cooking.')

def main():
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
    prompt = 'Please select an option by typing the corresponding number:'
    prompt += '\n1: Add a recipe'
    prompt += '\n2: Delete a recipe'
    prompt += '\n3: Print a recipe'
    prompt += '\n4: Print the cookbook'
    prompt += '\n5: Quit'
    print(prompt)
    while (True):
        try:
            value = int(input('>> '))
            assert (1 <= value <= 5)
        except:
            print('This option does not exist, please type the corresponding number.')
            print('To exit, enter 5.')
        else:
            if (value == 5):
                print('Cookbook closed.')
                break
            print(prompt)

if __name__ == '__main__':
    main()