#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from random import randint as rand

def main():
    print('This is an interactive guessing game!')
    print('You have to enter a number between 1 and 99 to find out the secret number.')
    print("Type 'exit' to end the game.")
    print('Good luck!')
    print()
    value_to_find = rand(1, 99)
    nb_try = 0
    while (True):
        value = input("What's your guess between 1 and 99\n>> ")
        if (value == 'exit'):
            print('Goodbye!')
            exit(0)
        else:
            try:
                value = (int(value))
                nb_try += 1
            except:
                print("That's not a number.")
            else:
                if (value == value_to_find):
                    if (value == 42):
                        print('The answer to the ultimate question of life, the universe and everything is 42.')
                    if (nb_try == 1):
                        print("Congratulations!, you've got it on your first try!")
                    else:
                        print("Congratulations, you've got it!")
                        print(f'You won in {nb_try} attempts!')
                    break
                if (value < value_to_find):
                    print('Too low!')
                if (value > value_to_find):
                    print('Too high!')

if __name__ == '__main__':
    main()
