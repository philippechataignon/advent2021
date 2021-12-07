#!/usr/bin/env python3

def fuel(l, pos):
    return sum([abs(x - pos) for x in l])

def main():
    with open("input.txt") as f:
        l = eval(f"[{f.readline()}]")
    l = [int(x) for x in l]

    m, mf = 0, 0
    for n in range(len(l) + 1):
        f = fuel(l, n)
        if n == 0 or f < mf:
            m, mf = n, f
    print(m, mf)

if __name__ == '__main__':
    main()

