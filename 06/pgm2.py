#!/usr/bin/env python3

from lanternfish import Lantern

def main():
    c = [0] * 9
    with open("input.txt") as f:
        l = eval(f"[{f.readline()}]")
    for n in l:
        c[n] += 1

    for i in range(256):
        print(c)
        tmp = c[0]
        for n in range(1,9):
            c[n-1] = c[n]
        c[8] = tmp
        c[6] += tmp

    print(sum(c))

if __name__ == '__main__':
    main()

