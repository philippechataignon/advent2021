#!/usr/bin/env python3
g = {}
C = 0
R = 0

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def get(g, r, c):
    if r < 0 or r >= R or c < 0 or c >= C:
        return 9
    else:
        return g.get((r, c), 0)

def islow(g, r, c):
    return all([get(g, r+dx, c+dy) > get(g, r, c) for dx,dy in dirs])

def getbasin(g, r, c, l=None):
    if l is None:
        l = {(r,c)}
    for dx, dy in dirs:
        x, y = r + dx, c + dy
        if (x, y) not in l and get(g, x, y) < 9:
            l.add((x, y))
            getbasin(g, x, y, l)
    return l

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
    lb = []
    for r in range(R):
        for c in range(C):
            if islow(g, r, c):
                b = getbasin(g, r, c)
                lb.append(len(b))
    lb.sort(reverse=True)
    print(lb[0] * lb[1] * lb[2])

if __name__ == '__main__':
    main()

