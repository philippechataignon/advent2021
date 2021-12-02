#!/usr/bin/env python3
def main():
    hor = 0
    depth = 0
    aim = 0
    with open("input.txt") as f:
        for l in f:
            l = l[:-1]
            c,n = l.split(" ")
            n = int(n)
            if c == "forward":
                hor += n
                depth += n * aim
            elif c == "down":
                aim += n
            elif c == "up":
                aim -= n
            print(c, n, hor, depth, aim)

    print(hor * depth)

if __name__ == '__main__':
    main()

