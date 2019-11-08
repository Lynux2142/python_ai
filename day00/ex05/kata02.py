#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import argv, stdout

def main():
    t = (3, 30, 2019, 9, 25)
    print(f'{t[0]:0>2}/{t[1]:0>2}/{t[2]:0>4} {t[3]:0>2}:{t[4]:0>2}')

if __name__ == '__main__':
    main()
