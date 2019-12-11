import math


def mass_to_fuel(mass):
    return math.floor(mass / 3) - 2


def total_fuel(mass):
    fuel = mass_to_fuel(mass)
    additional_fuel = fuel
    while additional_fuel >= 0:

        additional_fuel = mass_to_fuel(additional_fuel)
        if additional_fuel > 0:
            fuel += additional_fuel
    return fuel


def test_mass_to_fuel():
    assert mass_to_fuel(14) == 2
    assert mass_to_fuel(1969) == 654
    assert mass_to_fuel(100756) == 33583


def test_fuel_for_fuel():
    assert total_fuel(14) == 2
    assert total_fuel(1969) == 966
    assert total_fuel(100756) == 50346


if __name__ == "__main__":
    with open("inputs/day_1.txt") as f:
        lines = f.read().splitlines()
    numbers = list(map(lambda x: int(x), lines))  # I know, I know, use iterator, bla bla.
    part1Total = sum(map(lambda x: mass_to_fuel(x), numbers))
    part2Total = sum(map(lambda x: total_fuel(x), numbers))

    print(part1Total)
    print(part2Total)
