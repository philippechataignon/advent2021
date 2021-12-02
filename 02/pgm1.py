#!/usr/bin/env python3
def main():
    hor = 0
    depth = 0
    with open("input.txt") as f:
        for l in f:
            l = l[:-1]
            c,n = l.split(" ")
            n = int(n)
            print(c,n)
            if c == "forward":
                hor += n
            elif c == "down":
                depth += n
            elif c == "up":
                depth -= n

    print(hor * depth)

if __name__ == '__main__':
    main()

