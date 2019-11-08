#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import argv, stdout

def main():
    t = (0, 4, 132.42222, 10000, 12345.67)
    print(f"day_{t[0]:0>2}, ex_{t[1]:0>2} : {round(t[2], 2)}, {'%.2e'%t[3]}, {'%.2e'%t[4]}")

if __name__ == '__main__':
    main()
