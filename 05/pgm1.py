#!/usr/bin/env python3
def main():
    grid = {}
    with open("input.txt") as f:
        for l in f:
            l = l[:-1].split("->")
            x1, y1 = [int(x) for x in l[0].split(",")]
            x2, y2 = [int(x) for x in l[1].split(",")]
            # hor
            if x1 == x2:
                if y1 > y2:
                    y2, y1 = y1, y2
                for y in range(y1, y2+1):
                    grid[(x1, y)] = grid.get((x1, y), 0) + 1
            elif y1 == y2:
                if x1 > x2:
                    x2, x1 = x1, x2
                for x in range(x1, x2+1):
                    grid[(x, y1)] = grid.get((x, y1), 0) + 1
    nb = 0
    for x in grid.values():
        if x >= 2:
            nb += 1
    print(nb)

if __name__ == '__main__':
    main()

