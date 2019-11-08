#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import argv, exit

def main():
    if (len(argv) == 1):
        exit(0)
    try:
        assert (len(argv) == 2)
        assert (type(int(argv[1])) == int)
    except:
        print('ERROR')
        exit(1)
    value = int(argv[1])
    if (value == 0):
        print('I\'m Zero.')
    elif ((value % 2) == 0):
        print('I\'m Even.')
    else:
        print('I\'m Odd.')

if __name__ == '__main__':
    main()
