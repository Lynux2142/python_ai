#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import argv

def make_all_operations(n1, n2):
    Sum = n1 + n2
    Diff = n1 - n2
    Prod = n1 * n2
    Quot = None if (n2 == 0) else float(n1) / float(n2)
    Rema = None if (n2 == 0) else n1 % n2
    return (Sum, Diff, Prod, Quot, Rema)

def main():
    try:
        assert (len(argv) == 3)
        n1 = int(argv[1])
        n2 = int(argv[2])
    except ValueError:
        print(f'InputError: only numbers\n')
        print('Usage: python operations.py <number1> <number2>')
        print('Example:')
        print('     python operations.py 10 3')
    except:
        if (len(argv) > 2):
            print('InputError: too many arguments\n')
        print('Usage: python operations.py <number1> <number2>')
        print('Example:')
        print('     python operations.py 10 3')
    else:
        Sum, Diff, Prod, Quot, Rema = make_all_operations(n1, n2)
        print(f"{'Sum:':<14}{Sum}\n{'Difference:':<14}{Diff}\n{'Product:':<14}{Prod}\n{'Quotient:':<14}{'ERROR (div by zero)' if (not Quot) else Quot}\n{'Remainder:':<14}{'ERROR (modulo by zero)' if (not Rema) else Rema}")

if __name__ == '__main__':
    main()
