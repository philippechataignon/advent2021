#!/usr/bin/env python3
g = {}
C = 0
R = 0

def get(g, r, c):
    if r < 0 or r >= R or c < 0 or c >= C:
        return 0
    else:
        return g.get((r, c), 0)

def fold(sens, val):
    global g
    if sens == "y":
        for c in range(C):
            for r in range(val):
                if get(g, R - r - 1, c) == 1:
                    g[(r, c)] = 1       # reflet
                    g[(R - r - 1, c)] = 0   # efface origine
    elif sens == "x":
        for r in range(R):
            for c in range(val):
                if get(g, r, C - c -1) == 1:
                    g[(r, c)] = 1       # reflet
                    g[(r, C - c - 1)] = 0   # efface origine
    else:
        print("Error: sens")

def display(g):
    for r in range(R):
        print([get(g, r, c) for c in range(C)])

def main():
    global C,R
    f = open("input.txt")
    r = 0
    while True:
        l = f.readline()[:-1]
        if l == "":
            break
        c, r = map(int, l.split(","))
        g[(r, c)] = 1
        if r > R:
            R = r
        if c > C:
            C = c
    R += 1
    C += 1
    print(R, C)
    print(sum([get(g, r, c) for r in range(R) for c in range(C)]))
    cmd = f.readline()
    sens, val = cmd[11:-1].split("=")
    val = int(val)
    print(sens, val)
    fold(sens, val)
    print(sum([get(g, r, c) for r in range(R) for c in range(C)]))

if __name__ == '__main__':
    main()
