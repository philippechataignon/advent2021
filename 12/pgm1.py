#!/usr/bin/env python3
def main():
    adj = {}
    with open("test.txt") as f:
        for l in f:
            a, b = l[:-1].split("-")
            print(a,b)
            if not a in adj:
                adj[a] = []
            if not b in adj:
                adj[b] = []
            adj[a].append(b)
            adj[b].append(a)
    print(has_path(adj, "start", "end"))

def has_path(adj, src, dst, visited=None):
    if visited is None:
        visited = set()

    if (src == dst):
        return True

    if src in visited:
        return False

    if "a" <= src[0] <= "z":
        visited.add(src)

    for n in adj[src]:
        if has_path(adj, n, dst, visited):
            return True

    return False

if __name__ == '__main__':
    main()

