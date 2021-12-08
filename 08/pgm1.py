#!/usr/bin/env python3
def main():
    n = 0
    with open("input.txt") as f:
        for l in f:
            l = l[:-1].split(" | ")[1].split(" ")
            n += sum([len(x) in [2,3,4,7] for x in l])

    print(n)

if __name__ == '__main__':
    main()

