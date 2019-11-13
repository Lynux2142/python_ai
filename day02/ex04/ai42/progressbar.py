from time import sleep, time
from sys import stdout

def ft_progress(listy):
    begin = time()
    for i in listy:
        perc = int(float(i) / len(listy) * 100.0)
        progress = '=' * int(float(perc) / 100.0 * 50.0) + '>' if (perc < 100) else ''
        stdout.write(f"\r ETA: (?) [{perc:>3}%] [{progress:<50}] {i}/{len(listy)} | elapsed time {round((time() - begin), 2)}s")
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
