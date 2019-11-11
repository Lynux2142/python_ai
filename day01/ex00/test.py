#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from book import Book
from recipe import Recipe

def main():
    cookbook = Book()
    print(cookbook.creation_date)
    print(cookbook.last_update)
    test = Recipe()
    cookbook.add_recipe(test)
    test = Recipe()
    cookbook.add_recipe(test)
    test = Recipe()
    cookbook.add_recipe(test)
    print(cookbook.get_recipe_by_type('lunch'))
    print(cookbook.creation_date)
    print(cookbook.last_update)

if __name__ == '__main__':
    main()
