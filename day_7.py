from collections import deque
from itertools import permutations

inputs = deque()


# outputs = deque()


def parse_opcode(arr, index):
    code = str(arr[index])
    op = int(code[-2:])
    modes = [0, 0, 0]

    if len(code) > 1:
        rest = list(reversed(code[:-2]))  # 10
        for i in range(len(rest)):
            modes[i] = int(rest[i])

    def first():
        return arr[arr[index + 1]] if modes[0] == 0 else arr[index + 1]

    def second():
        return arr[arr[index + 2]] if modes[1] == 0 else arr[index + 2]

    if op == 1 or op == 2:
        first = first()
        second = second()
        out = arr[index + 3]
        arr[out] = first + second if op == 1 else first * second
        return arr, index + 4, 0
    elif op == 3:
        arr[arr[index + 1]] = int(inputs.popleft())
        return arr, index + 2, 0
    elif op == 4:
        inputs.append((arr[arr[index + 1]] if modes[0] == 0 else arr[index + 1]))
        return arr, index + 2, 1
    elif op == 5:
        return arr, index + 3 if first() == 0 else second(), 0
    elif op == 6:
        return arr, index + 3 if first() != 0 else second(), 0
    elif op == 7:
        arr[arr[index + 3]] = 1 if first() < second() else 0
        return arr, index + 4, 0
    else:  # op == 8
        arr[arr[index + 3]] = 1 if first() == second() else 0
        return arr, index + 4, 0


def run_program(arr, index=0):
    while arr[index] != 99:
        arr, index, pause = parse_opcode(arr, index)
        if pause == 1:
            return arr, index
    return arr, -1


def run_thrusters(arr, seq):
    inputs.clear()
    N = len(seq)
    for i in range(N):
        if i == 0:
            inputs.appendleft(0)

        inputs.appendleft(seq[i])
        cpy = arr.copy()

        run_program(cpy)

        if i == N - 1:
            return inputs.pop()


def loop_thrusters(arr, seq):
    inputs.clear()
    N = len(seq)
    i = 0
    first_run = True
    first_amp = True
    programs = [arr.copy() for _ in range(N)]
    pcs = [0 for _ in range(N)]
    i = 0
    while True:

        if i == 0 and first_amp:
            inputs.appendleft(0)
            first_amp = False

        if first_run:
            inputs.appendleft(seq[i])

        if pcs[i] != -1:
            _, index = run_program(programs[i], pcs[i])
            pcs[i] = index

        i += 1
        if i % 5 == 0:
            i %= 5
            first_run = False
            
        if all([x == -1 for x in pcs]):
            return inputs.pop()


def test_thrusters():
    assert run_thrusters([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [4, 3, 2, 1, 0]) == 43210
    assert run_thrusters(
        [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
        [0, 1, 2, 3, 4]) == 54321
    assert run_thrusters(
        [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31,
         31, 4, 31, 99, 0, 0, 0], [1, 0, 4, 3, 2]) == 65210

    assert loop_thrusters([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                    27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], [9, 8, 7, 6, 5]) == 139629729

    assert loop_thrusters([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                           -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                           53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10], [9, 8, 7, 6, 5]) == 18216

if __name__ == "__main__":
    with open("inputs/day_7.txt") as f:
        program = f.read().split(",")

    N = 5
    codes = list(map(lambda x: int(x), program))
    max_power = 0
    for i in permutations([0, 1, 2, 3, 4]):
        current_power = run_thrusters(codes, list(i))
        max_power = max(max_power, current_power)

    print(max_power)  # End of part 1

    max_power = 0
    for i in permutations([5,6,7,8,9]):
        current_power = loop_thrusters(codes, list(i))
        max_power = max(max_power, current_power)

    print(max_power)  # End of part 2
