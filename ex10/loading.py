#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from time import sleep
from sys import stdout

def ft_progress(listy):
    for i in listy:
        perc = int(float(i) / len(listy) * 100.0)
        stdout.write(f"\r ETA: (time) [{perc:>3}%] [{'>':=>50}] {i}/{len(listy)} | elapsed time (time)")
        yield i

def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)

if __name__ == '__main__':
    main()
