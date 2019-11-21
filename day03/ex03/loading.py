#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from time import sleep, time
from sys import stdout

def ft_progress(listy):
    begin = time()
    for i in listy:
        value = i + 1
        perc = int(float(value) / len(listy) * 100.0)
        progress = '=' * int(float(perc) / 100.0 * 50.0) + ('>' if (perc < 100) else '')
        actual_time = round((time() - begin), 2)
        eta_time = int(round(actual_time * (100 - perc) / (perc if (perc) else 1), 0))
        stdout.write(f"\r ETA: ({eta_time:>4}s) [{perc:>3}%] [{progress:<50}] {value}/{len(listy)} | elapsed time {actual_time}s")
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
