import math
def has_two_adjacent_pt1(n):
    n = str(n)
    return n[0] == n[1] or n[1] == n[2] or n[2] == n[3] or n[3] == n[4] or n[4] == n[5]

def has_two_adjacent(n):
    n = str(n)
    l = len(n)

    current = n[0]
    count = 1
    for i in range(1, l):
        if n[i] == current:
            count += 1
        else:
            if count == 2:
                return True
            count = 1
            current = n[i]

    if count == 2:
        return True
    return False


def is_non_descending(n):
    n = str(n)
    return n[0] <= n[1] <= n[2] <= n[3] <= n[4] <= n[5]


def predicate(number):
    len = int(math.log10(number)) + 1
    return len == 6 and has_two_adjacent(number) and is_non_descending(number)


def test_predicate():
    assert predicate(112233)
    assert not predicate(123444)
    assert predicate(111122)


if __name__ == "__main__":
    results = [i for i in range(172930, 683082) if predicate(i)]
    print(results)
    print(len(results))
