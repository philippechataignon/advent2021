#!/usr/bin/env python3
import numpy as np

def main():
    gr = []
    with open("input.txt") as f:
        nums = np.array(eval(f"[{f.readline()}]"))
        while True:
            blank = f.readline()
            if not blank:
                break
            gr.append(np.loadtxt(f, dtype=np.int32, max_rows=5))
    found = False
    res = [0] * len(gr)

    for n in nums:
        for i, g in enumerate(gr):
            r = np.where(g == n)
            g[r] = -1

            s0 = np.sum(g, axis=0)
            if np.any(s0 == -5):
                res[i] = 1
                if sum(res) == len(gr):
                    found = True
                    break

            s1 = np.sum(g, axis=1)
            if np.any(s1 == -5):
                res[i] = 1
                if sum(res) == len(gr):
                    found = True
                    break

        if found:
            a = sum(g[np.where(g != -1)])
            print(a * n)
            break

if __name__ == '__main__':
    main()

