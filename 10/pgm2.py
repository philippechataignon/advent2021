#!/usr/bin/env python3

pts = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
dlm = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

def test(s):
    stack = list()
    for c in s:
        if c in dlm.values():
            stack.append(c)
        elif c in dlm:
            d = stack.pop()
            if dlm[c] != d:
                return False, stack
    return True, stack

def main():
    scores = []
    with open("input.txt") as f:
        for l in f:
            l = l[:-1]
            t, stack = test(l)
            score = 0
            if t:
                for c in reversed(stack):
                    score = 5 * score + pts[c]
                scores.append(score)
    scores.sort()
    print(scores[len(scores) // 2])

if __name__ == '__main__':
    main()
