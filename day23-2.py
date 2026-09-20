# https://adventofcode.com/2019/day/23
import importlib

day23 = importlib.import_module("day23-1")


def part2(input_file):
  return day23.run_network(day23.load_program(input_file), True)


def main():
  input_file = "day23-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
