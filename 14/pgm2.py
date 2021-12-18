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
    duo_start = [start[i:i+2] for i in range(len(start) - 1)]
    print(start, duo_start)
    f.readline()
    cmd_duo = {}
    cmd_let = {}
    while True:
        l = f.readline()
        if l == "":
            break
        p, m = l[:-1].split(" -> ")
        cmd_duo[p] = [p[0] + m, m + p[1]]
        cmd_let[p] = m
    print(cmd_duo, cmd_let)
    let_count = {}
    duo_count = {}
    for k in cmd_duo:
        duo_count[k] = 0
    for c in duo_start:
        duo_count[c] += 1
    for k in cmd_let.values():
        let_count[k] = 0
    for c in start:
        let_count[c] += 1
    for i in range(40):
        eff = duo_count.copy()
        for x in duo_count:
            n = eff[x]
            duo_count[x] -= n
            t = cmd_duo[x]
            duo_count[t[0]] += n
            duo_count[t[1]] += n
            l = cmd_let[x]
            let_count[l] += n
    print(let_count)
    print(max(let_count.values()) - min(let_count.values()))

if __name__ == '__main__':
    main()

