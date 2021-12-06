#!/usr/bin/env python3

from lanternfish import Lantern

def main():
    with open("input.txt") as f:
        l = eval(f"[{f.readline()}]")
    l = [Lantern(n) for n in l]
    print(l)
    for i in range(80):
        l = [x for n in l for x in n.tick()]
    print(len(l))


if __name__ == '__main__':
    main()

