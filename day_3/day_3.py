def manhattan_dist(first, second=(0, 0)):
    x1, y1 = first
    x2, y2 = second
    return abs(x1 - x2) + abs(y1 - y2)


def process_steps(steps):
    x, y = 0, 0
    for step in steps:
        direction, offset = step[0], int(step[1:])

        for i in range(1, offset + 1):
            if direction == 'L':
                yield (x - i, y)
            elif direction == 'R':
                yield (x + i, y)
            elif direction == 'U':
                yield (x, y - i)
            else:
                yield (x, y + i)

        if direction == 'L':
            x -= offset
        elif direction == 'R':
            x += offset
        elif direction == 'U':
            y -= offset
        else:
            y += offset


def run_wires(wire_1, wire_2):
    final = set(process_steps(wire_1))
    return min(manhattan_dist(x) for x in process_steps(wire_2) if x in final)


def nearest_intersection(wire_1, wire_2):
    path_1 = list(process_steps(wire_1))
    path_2 = list(process_steps(wire_2))
    return min([path_1.index(intersect) + path_2.index(intersect) + 2 for intersect in set(path_1).intersection(set(path_2))])


def test_run_wires():
    assert run_wires(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]) == 6
    assert run_wires(["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
                     ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]) == 135
    assert run_wires(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                     ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]) == 159


def test_nearest_intersection():
    assert nearest_intersection(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]) == 30
    assert nearest_intersection(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]) == 610
    assert nearest_intersection(["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
                                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]) == 410


if __name__ == "__main__":
    with open("../inputs/day_3.txt") as f:
        wire_1 = f.readline().split(",")
        wire_2 = f.readline().split(",")

    #test_run_wires()
    #print(run_wires(wire_1, wire_2))
    print(nearest_intersection(wire_1, wire_2))
