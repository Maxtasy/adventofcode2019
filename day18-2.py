# https://adventofcode.com/2019/day/18
import importlib

day18 = importlib.import_module("day18-1")


def part2(input_file):
  grid = day18.load_grid(input_file)
  sx, sy = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "@")

  # split the vault into four quadrants
  for dy in (-1, 0, 1):
    for dx in (-1, 0, 1):
      grid[sy + dy][sx + dx] = "#"
  for dy in (-1, 1):
    for dx in (-1, 1):
      grid[sy + dy][sx + dx] = "@"

  return day18.solve(grid)


def main():
  input_file = "day18-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
