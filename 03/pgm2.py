#!/usr/bin/env python3
def main():
    with open("input.txt") as f:
        r = [list(l[:-1]) for l in f]
    l = len(r[0])   #nb cols

    r1 = r.copy()
    i = 0
    while i < l and len(r1) > 1:
        ones = sum([1 if x[i] == '1' else 0 for x in r1])
        bit = "1" if ones >= len(r1) / 2 else "0"
        r1 = [x for x in r1 if x[i] == bit]
        i += 1
    a = eval("0b" + "".join(r1[0]))

    r2 = r.copy()
    i = 0
    while i < l and len(r2) > 1:
        ones = sum([1 if x[i] == '1' else 0 for x in r2])
        bit = "0" if ones >= len(r2) / 2 else "1"
        r2 = [x for x in r2 if x[i] == bit]
        i += 1
    b = eval("0b" + "".join(r2[0]))
    print(a * b)

if __name__ == '__main__':
    main()

