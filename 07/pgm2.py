#!/usr/bin/env python3

def fuel(l, pos, d):
    return sum([d[abs(x - pos)] for x in l])

def main():
    with open("input.txt") as f:
        l = eval(f"[{f.readline()}]")
    l = [int(x) for x in l]

    m, mf = 0, 0
    d = {}
    d[0] = 0
    for n in range(1, max(l) - min(l) + 1):
        d[n] = d[n-1] + n
    print(d)

    for n in range(min(l), max(l) + 1):
        f = fuel(l, n, d)
        if n == 0 or f < mf:
            m, mf = n, f
    print(m, mf)

if __name__ == '__main__':
    main()

