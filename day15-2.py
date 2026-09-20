# https://adventofcode.com/2019/day/15
import importlib

day15 = importlib.import_module("day15-1")


def part2(input_file):
  grid, oxygen = day15.explore(day15.load_program(input_file))
  return max(day15.bfs(grid, oxygen).values())


def main():
  input_file = "day15-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
