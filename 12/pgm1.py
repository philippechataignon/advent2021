#!/usr/bin/env python3
def main():
    adj = {}
    with open("input.txt") as f:
        for l in f:
            a, b = l[:-1].split("-")
            if not a in adj:
                adj[a] = []
            if not b in adj:
                adj[b] = []
            adj[a].append(b)
            adj[b].append(a)
    get_path(adj, "start", "end")

def get_path(adj, src, dst, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if "a" <= src[0] <= "z":
        visited.add(src)

    path.append(src)

    if (src == dst):
        print(path)
    else:
        for n in adj[src]:
            if n not in visited:
                r = get_path(adj, n, dst, visited, path)
    path.pop()
    if src in visited:
        visited.remove(src)

if __name__ == '__main__':
    main()
