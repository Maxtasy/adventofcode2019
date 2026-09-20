# https://adventofcode.com/2019/day/7
from itertools import permutations
from intcode import Intcode, load_program


def part2(input_file):
  program = load_program(input_file)
  best = 0

  for phases in permutations(range(5, 10)):
    amps = [Intcode(program, [p]) for p in phases]
    signal = 0
    last_e = None

    while not any(a.halted for a in amps):
      for i, amp in enumerate(amps):
        amp.inputs.append(signal)
        out = amp.step_output()
        if out is None:
          break
        signal = out
        if i == len(amps) - 1:
          last_e = signal

    best = max(best, last_e)

  return best


def main():
  input_file = "day07-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
