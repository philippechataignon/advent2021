#!/usr/bin/env python3

pts = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
dlm = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

stack = list()

def test(s):
    for c in s:
        if c in dlm.values():
            stack.append(c)
        elif c in dlm:
            d = stack.pop()
            if dlm[c] != d:
                return pts[c]
        else:
            print("Uncorrect:", c)
    return None

def main():
    with open("input.txt") as f:
        somme = 0
        for l in f:
            l = l[:-1]
            t = test(l)
            if t is not None:
                somme += t
        print(somme)

if __name__ == '__main__':
    main()

