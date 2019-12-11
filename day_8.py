def chunk(arr, size):
    for i in range(0, len(arr), size):
        yield (arr[i: i + size])


if __name__ == "__main__":
    width = 25
    height = 6
    per_layer = width * height
    with open("inputs/day_8.txt") as f:
        data = f.read()

    digits = list()

    layers = list(chunk(list(map(lambda x: int(x), data)), per_layer))

    min_zeros = per_layer
    min_layer = None
    for layer in layers:
        zero_count = len([x for x in layer if x == 0])
        if min_zeros > zero_count:
            min_layer = layer
            min_zeros = zero_count

    ones_count = len([x for x in min_layer if x == 1])
    twos_count = len([x for x in min_layer if x == 2])

    print(ones_count * twos_count)

    result = []
    for i in range(per_layer):
        pixel = 2
        for layer in layers:
            if layer[i] != 2:
                pixel = layer[i]
                break
        result.append(pixel)

    for chnk in chunk(result, width):
        for j in range(width):
            print("█" if chnk[j] == 1 else "░", end="")
        print("")
