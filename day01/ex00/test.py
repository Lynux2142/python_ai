#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from book import Book
from recipe import Recipe

def main():
    cookbook = Book()
    print(cookbook.creation_date)
    print(cookbook.last_update)
    test = Recipe()
    cookbook.add_recipe(test)
    print(str(cookbook.recipes_list['lunch'][0]))
    print(cookbook.creation_date)
    print(cookbook.last_update)

if __name__ == '__main__':
    main()
