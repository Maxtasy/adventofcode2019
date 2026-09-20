# https://adventofcode.com/2019/day/9
from intcode import Intcode, load_program


def part1(input_file):
  outputs = Intcode(load_program(input_file), [1]).run_all()
  assert len(outputs) == 1, "self-test failed: %s" % outputs
  return outputs[0]


def main():
  input_file = "day09-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
