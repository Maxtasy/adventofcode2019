# https://adventofcode.com/2019/day/17
from intcode import Intcode, load_program


def get_grid(program):
  output = Intcode(program).run_all()
  return "".join(map(chr, output)).strip().split("\n")


def part1(input_file):
  grid = get_grid(load_program(input_file))
  total = 0
  for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[y]) - 1):
      if all(grid[y + dy][x + dx] == "#" for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))):
        total += x * y
  return total


def main():
  input_file = "day17-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
