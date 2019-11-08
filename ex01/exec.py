#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import argv, stdout

def main():
    for i in range(len(argv) - 1, 0, -1):
        for letter in argv[i][::-1]:
            if (letter.isupper()):
                stdout.write(letter.lower())
            elif(letter.islower()):
                stdout.write(letter.upper())
            else:
                stdout.write(letter)
        if (i > 1):
            stdout.write(' ')
    if (len(argv) > 1):
        print()

if __name__ == '__main__':
    main()
