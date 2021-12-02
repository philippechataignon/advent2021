#!/usr/bin/env python3
def main():
    with open("input.txt") as f:
    # with open("test.txt") as f:
        lines = [int(x[:-1]) for x in f.readlines()]
    mm3 = [(lines[i] + lines[i+1] + lines[i+2]) for i in range(len(lines)-2)]
    print(mm3)
    incr = [0 if i == 0 else 1 if mm3[i] > mm3[i-1] else 0 for i in range(len(mm3))]
    print(sum(incr))

if __name__ == '__main__':
    main()



if __name__ == '__main__':
    main()

