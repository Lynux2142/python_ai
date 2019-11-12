#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from vector import Vector

def main():
    v1 = Vector((10, 14))
    print(f'v1: {v1}')
    v2 = Vector([2, 4, 6, 8])
    print(f'v2: {v2}')
    v3 = Vector(4)
    print(f'v3: {v3}')
    v4 = v2 + v3
    print(f'v4: {v4}')
    v5 = 10 - v1
    print(f'v5: {v5}')
    v6 = v3 / 2
    print(f'v6: {v6}')
    dot = v1 * v2
    print(f'v1 dot v2: {dot}')

if __name__ == '__main__':
    main()
