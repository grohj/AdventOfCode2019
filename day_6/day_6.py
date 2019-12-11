from collections import deque
def parse(rel):
    return tuple(rel.split(")"))

with open("../inputs/day_6.txt") as f:
    pairs = f.read().splitlines()

def uniq():
    for pair in pairs:
        x,y = parse(pair)
        yield(x)
        yield(y)


if __name__ == "__main__":
    nodes = set(uniq())
    rel2 = {v:k for k,v in map(lambda x: parse(x), pairs)}
    rel = {v:k for k,v in map(lambda x: parse(x), pairs)}


    total = 0
    for node in nodes:
        ctr = 0
        while node in rel:
            node = rel[node]
            ctr += 1
        total += ctr

    print(total)


    rel.update(rel2)

    current = "YOU"
    visited = set(current)
    next = deque()
    next.append(current)
    ctr = 0
    while "SAN" not in next:

        new = deque()
        while len(next) != 0:
            n = next.popleft()
            visited.add(n)
            for x in [rel[x] for x in rel if n in x and rel[x] not in visited]:
                next.append(x)

        next = new
        ctr += 1

    print(ctr)


