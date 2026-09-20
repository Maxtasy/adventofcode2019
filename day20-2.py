# https://adventofcode.com/2019/day/20
import importlib

day20 = importlib.import_module("day20-1")


def part2(input_file):
  return day20.shortest(day20.load_maze(input_file), True)


def main():
  input_file = "day20-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
