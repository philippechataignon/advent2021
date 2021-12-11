#!/usr/bin/env python3
def sortstr(s):
    return "".join(sorted(list(s)))

conv = {
        "abcefg":0,
        "cf":1,
        "acdeg":2,
        "acdfg":3,
        "bcdf":4,
        "abdfg":5,
        "abdefg":6,
        "acf":7,
        "abcdefg":8,
        "abcdfg":9
}

def strin(s, target):
    return len(set(list(s)) - set(list(target))) == 0

def main():
    somme = 0
    with open("input.txt") as f:
        for l in f:
            d = l[:-1].split(" | ")[0].split(" ")
            a = l[:-1].split(" | ")[1].split(" ")
            d = list(map(sortstr, d))
            a = list(map(sortstr, a))

            digit = {}
            p = {}
            l5 = []
            l6 = []
            for s in d:
                if len(s) == 2:
                    digit[1] = s
                    p[s] = 1
                elif len(s) == 4:
                    digit[4] = s
                    p[s] = 4
                elif len(s) == 3:
                    digit[7] = s
                    p[s] = 7
                elif len(s) == 7:
                    digit[8] = s
                    p[s] = 8
                elif len(s) == 5:
                    l5.append(s)
                elif len(s) == 6:
                    l6.append(s)

            for w in l6:
                if not strin(digit[7], w):
                    digit[6] = w
                    p[w] = 6
                elif strin(digit[4], w):
                    digit[9] = w
                    p[w] = 9
                else:
                    digit[0] = w
                    p[w] = 0

            for w in l5:
                if strin(digit[7], w):
                    digit[3] = w
                    p[w] = 3
                elif strin(w, digit[9]):
                    digit[5] = w
                    p[w] = 5
                else:
                    digit[2] = w
                    p[w] = 2

            n = 0
            for w in a:
                n = n * 10 + int(p[w])
            print(n)
            somme += n
    print(somme)

if __name__ == '__main__':
    main()
    #print(strin("abdfg", "abcdfg"))
