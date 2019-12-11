from collections import deque, defaultdict
from itertools import groupby

def parse(rel):
    return tuple(rel.split(")"))

with open("inputs/day_6.txt") as f:
    pairs = f.read().splitlines()

def uniq():
    for pair in pairs:
        x,y = parse(pair)
        yield(x)
        yield(y)


if __name__ == "__main__":
    nodes = set(uniq())
    rel = {v:k for k,v in map(lambda x: parse(x), pairs)}

    rel2 = {k:v for k,v in groupby(map(lambda x: parse(x), pairs))}

    total = 0
    for node in nodes:
        ctr = 0
        while node in rel:
            node = rel[node]
            ctr += 1
        total += ctr

    print(total) # End of part 1

    rel, rel2 = defaultdict(list), defaultdict(list)
    
    for a,b in map(lambda x: parse(x), pairs):
        rel[a].append(b)
        rel2[b].append(a)


    current = "YOU"
    visited = set()
    visited.add(current)
    next = deque()
    next.append(current)
    ctr = 0
    while "SAN" not in next:

        new = deque()
        while len(next) != 0:
            n = next.popleft()
            visited.add(n)

            if n in rel:
                new.extend([x for x in rel[n] if x not in visited])
            if n in rel2:
                new.extend([x for x in rel2[n] if x not in visited])

        next = new
        ctr += 1

    print(ctr-2) # End of part 2


