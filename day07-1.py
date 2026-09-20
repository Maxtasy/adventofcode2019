# https://adventofcode.com/2019/day/7
from itertools import permutations
from intcode import Intcode, load_program


def part1(input_file):
  program = load_program(input_file)
  best = 0

  for phases in permutations(range(5)):
    signal = 0
    for phase in phases:
      signal = Intcode(program, [phase, signal]).run_all()[-1]
    best = max(best, signal)

  return best


def main():
  input_file = "day07-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
