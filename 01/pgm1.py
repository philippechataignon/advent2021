#!/usr/bin/env python3
def main():
    with open("input.txt") as f:
        lines = [int(x[:-1]) for x in f.readlines()]
    incr = [0 if i == 0 else 1 if lines[i] > lines[i-1] else 0 for i in range(len(lines))]
    print(sum(incr))

if __name__ == '__main__':
    main()

