# https://adventofcode.com/2019/day/19
from intcode import Intcode, load_program


def in_beam(program, x, y):
  return Intcode(program, [x, y]).run_all()[0] == 1


def part1(input_file):
  program = load_program(input_file)
  return sum(in_beam(program, x, y) for y in range(50) for x in range(50))


def main():
  input_file = "day19-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
