#!/usr/bin/env python3
def is_small(node):
    return node not in ("start", "end") and "a" <= node[0] <= "z"

res = set()

def main():
    global res
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
    visit = {}
    for node, neigh in adj.items():
        if node == "start":
            visit[node] = 0
        elif node == "end":
            visit[node] = 1
        elif is_small(node):
            visit[node] = 1
        else:
            visit[node] = 999999999
        visit["joker"] = 1

    lvisit = []
    for node in adj:
        if is_small(node):
            v = visit.copy()
            v[node] += 1 # this node can be twice
            lvisit.append(v)

    for visit in lvisit:
        get_path(adj, "start", "end", visit)

    print(len(res))

def get_path(adj, src, dst, visit, joker=True, path=None):
    global res
    if path is None:
        path = []

    visit[src] -= 1

    path.append(src)
    if (src == dst):
        res.add(tuple(path))
    else:
        for n in adj[src]:
            if visit[n] > 0:
                r = get_path(adj, n, dst, visit, joker, path)
    path.pop()
    visit[src] += 1

if __name__ == '__main__':
    main()
