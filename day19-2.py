# https://adventofcode.com/2019/day/19
from intcode import Intcode, load_program

SIZE = 100


def in_beam(program, x, y):
  return Intcode(program, [x, y]).run_all()[0] == 1


def part2(input_file):
  program = load_program(input_file)

  # Follow the bottom-left edge of the beam row by row; the square's top-right corner must also be in the beam.
  x = 0
  y = SIZE
  while True:
    while not in_beam(program, x, y):
      x += 1
    if in_beam(program, x + SIZE - 1, y - SIZE + 1):
      return x * 10000 + (y - SIZE + 1)
    y += 1


def main():
  input_file = "day19-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
