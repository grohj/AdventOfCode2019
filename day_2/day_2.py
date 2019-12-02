def handle_opcode(arr, index):
    left = arr[arr[index + 1]]
    right = arr[arr[index + 2]]
    arr[arr[index + 3]] = left + right if arr[index] == 1 else left * right
    return arr, index + 4


def run_program(arr):
    index = 0
    while arr[index] != 99:
        arr, index = handle_opcode(arr, index)
    return arr


def test_run_program():
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert run_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def find_correct(og_arr):

    for noun in range(100):  # By using very scientific tools, I determined this is enough.
        for verb in range(1000):
            try:
                arr = og_arr.copy()
                arr[1] = noun
                arr[2] = verb
                arr = run_program(arr)
                if arr[0] == 19690720:
                    return noun, verb
            except Exception:
                pass
    return None, None


if __name__ == "__main__":
    with open("../inputs/day_2.txt") as f:
        separated = f.read().split(",")

    arr = list(map(lambda x: int(x), separated))
    og_arr = arr.copy()
    arr[1] = 12
    arr[2] = 2
    print(run_program(arr)) # End of part one
    first, second = find_correct(og_arr)

    print("Part 2 answer is: {}".format(first * 100 + second)) # End of part two
