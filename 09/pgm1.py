#!/usr/bin/env python3
g = {}
C = 0
R = 0

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def get(g, r, c):
    if r < 0 or r >= R or c < 0 or c >= C:
        return 10
    else:
        return g.get((r, c), 0)

def islow(g, r, c):
    return all([get(g, r+dx, c+dy) > get(g, r, c) for dx,dy in dirs])

def main():
    global C,R
    f = open("input.txt")
    r = 0
    while True:
        l = f.readline()
        if not l:
            break
        l = [int(x) for x in l[:-1]]
        C = len(l)
        for c, v in enumerate(l):
            g[r, c] = v
        r += 1
    R = r

    s = 0
    for r in range(R):
        for c in range(C):
            if islow(g, r, c):
                #print(r, c, get(g, r, c))
                s += get(g, r, c) + 1
    print(s)

if __name__ == '__main__':
    main()

