#!/usr/bin/env python3
def apply(cmd, poly):
    ret = poly[0]
    for s in range(1, len(poly)):
        state = poly[s - 1]
        ret += cmd[state][poly[s]]
    return ret

def main():
    f = open("input.txt")
    start = f.readline()[:-1]
    # start = list(start)
    print(start)
    f.readline()
    cmd = {}
    while True:
        l = f.readline()
        if l == "":
            break
        p, m = l[:-1].split(" -> ")
        if p[0] not in cmd:
            cmd[p[0]] = {}
        cmd[p[0]][p[1]] = m + p[1]
    print(cmd)
    s = start
    for i in range(10):
        s = apply(cmd, s)
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    print(max(count.values()) - min(count.values()))

if __name__ == '__main__':
    main()

