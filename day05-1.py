# https://adventofcode.com/2019/day/5
from intcode import Intcode, load_program


def part1(input_file):
  outputs = Intcode(load_program(input_file), [1]).run_all()
  assert all(o == 0 for o in outputs[:-1]), "diagnostic tests failed"
  return outputs[-1]


def main():
  input_file = "day05-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
