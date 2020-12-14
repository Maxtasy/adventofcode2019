# https://adventofcode.com/2019/day/1


def get_fuel_needed(mass):
  total_fuel = 0
  fuel_mass = mass
  while True:
    fuel_mass = fuel_mass//3-2
    if fuel_mass > 0:
      total_fuel += fuel_mass
    else:
      break
  
  return total_fuel


def part1(input_file):
  with open(input_file, "r") as f:
    masses = list(map(int, f.read().strip().split("\n")))

    total_fuel = 0

    for mass in masses:
      total_fuel += get_fuel_needed(mass)

    return total_fuel


def main():
  input_file = "day01-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()