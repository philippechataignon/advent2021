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
    # print(nums)
    # print(gr)
    found = False

    for n in nums:
        # print("n=", n)
        for g in gr:
            # print("g=", g)
            r = np.where(g == n)
            g[r] = -1

            s0 = np.sum(g, axis=0)
            if np.any(s0 == -5):
                found = True
                break

            s1 = np.sum(g, axis=1)
            if np.any(s1 == -5):
                found = True
                break
        if found:
            a = sum(g[np.where(g != -1)])
            print(a * n)
            break

if __name__ == '__main__':
    main()

