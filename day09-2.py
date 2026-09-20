# https://adventofcode.com/2019/day/9
from intcode import Intcode, load_program


def part2(input_file):
  return Intcode(load_program(input_file), [2]).run_all()[-1]


def main():
  input_file = "day09-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
