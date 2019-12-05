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
        return arr, index + 4
    elif op == 3:
        print("I need input:")
        arr[arr[index + 1]] = int(input())
        return arr, index + 2
    elif op == 4:
        print(arr[arr[index + 1]] if modes[0] == 0 else arr[index + 1])
        return arr, index + 2
    elif op == 5:
        return arr, index + 3 if first() == 0 else second()
    elif op == 6:
        return arr, index + 3 if first() != 0 else second()
    elif op == 7:
        arr[arr[index + 3]] = 1 if first() < second() else 0
        return arr, index + 4
    else:  # op == 8
        arr[arr[index + 3]] = 1 if first() == second() else 0
        return arr, index + 4


def run_program(arr):
    index = 0
    while arr[index] != 99:
        arr, index = parse_opcode(arr, index)
    return arr


def test_run_program():
    assert run_program([1002, 4, 3, 4, 33])[4] == 99
    assert run_program([1101, 100, -1, 4, 0])[4] == 99
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert run_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def manual_test():
    print("Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).")
    run_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8])
    print("Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).")
    run_program([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8])
    print("Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).")
    run_program([3, 3, 1108, -1, 8, 3, 4, 3, 99])
    print("Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).")
    run_program([3, 3, 1107, -1, 8, 3, 4, 3, 99])
    print(
        "Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:")
    run_program([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9])
    run_program([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])

    print("""The below example program uses an input instruction to ask for a single number. The program will then output 
    999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input 
    value is greater than 8. """)

    run_program(
        [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
         4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])


if __name__ == "__main__":
    with open("../inputs/day_5.txt") as f:
        program = f.read().split(",")

    codes = list(map(lambda x: int(x), program))

    run_program(codes)
