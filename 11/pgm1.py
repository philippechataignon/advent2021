#!/usr/bin/env python3

class cell:
    C = 10
    R = 10
    dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1, -1), (1,-1), (-1, 1)]
    def __init__(self, g, r, c, v):
        self.g = g
        self.r = r
        self.c = c
        self.v = v
        self.has_flash = False
        self.nb_flash = 0

    def add1(self):
        self.v += 1
        if self.v > 9:
            self.flash()

    def flash(self):
        if not self.has_flash:
            self.has_flash = True
            for dx, dy in cell.dirs:
                x = self.r + dx
                y = self.c + dy
                if not(x < 0 or x >= cell.R or y < 0 or y >= cell.C):
                    self.g[x, y].add1()

    def endstep(self):
        if self.has_flash:
            self.v = 0
            self.nb_flash += 1
            self.has_flash = False

def step(g):
    global nb_flash
    for r in range(cell.R):
        for c in range(cell.C):
            g[(r, c)].add1()

    for r in range(cell.R):
        for c in range(cell.C):
            g[(r, c)].endstep()

def print_g(g):
    for r in range(cell.R):
        for c in range(cell.C):
            print(g[(r, c)].v, end="")
        print()
    print()

def main():
    g = {}
    f = open("input.txt")
    r = 0
    while True:
        l = f.readline()
        if not l:
            break
        l = [int(x) for x in l[:-1]]
        for c, v in enumerate(l):
            g[r, c] = cell(g, r, c, v)
        r += 1
    print_g(g)
    for i in range(100):
        step(g)
        print_g(g)
    print(sum([x.nb_flash for x in g.values()]))

if __name__ == '__main__':
    main()
