#!/usr/bin/env python3
def main():
    with open("input.txt") as f:
        r = [list(l[:-1]) for l in f]
    l = len(r[0])
    n = len(r)
    ones = [0] * l
    for i in range(l):
        ones[i] = sum([1 if x[i] == '1' else 0 for x in r])
    a = eval("0b" + "".join(["1" if ones[i] >= n // 2 else "0" for i in range(l)]))
    b = eval("0b" + "".join(["0" if ones[i] >= n // 2 else "1" for i in range(l)]))
    print(a*b, a, b)

if __name__ == '__main__':
    main()

