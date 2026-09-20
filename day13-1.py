# https://adventofcode.com/2019/day/13
from intcode import Intcode, load_program


def part1(input_file):
  outputs = Intcode(load_program(input_file)).run_all()
  return sum(1 for i in range(2, len(outputs), 3) if outputs[i] == 2)


def main():
  input_file = "day13-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
