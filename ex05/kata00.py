#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import stdout

def main():
    t = (19, 42, 21)
    stdout.write(f'The {len(t)} numbers are: ')
    for i in range(0, len(t)):
        stdout.write(f'{t[i]}')
        if (i < len(t) - 1):
            stdout.write(', ')
    print()

if __name__ == '__main__':
    main()
