# https://adventofcode.com/2019/day/21
from intcode import Intcode, load_program

# Jump if there is a hole in A, B or C, but only if D (landing tile) is ground.
SCRIPT = [
  "NOT A J",
  "NOT B T",
  "OR T J",
  "NOT C T",
  "OR T J",
  "AND D J",
  "WALK",
]


def run_springdroid(input_file, script):
  text = "\n".join(script) + "\n"
  output = Intcode(load_program(input_file), [ord(c) for c in text]).run_all()
  if output[-1] > 255:
    return output[-1]
  raise Exception("Droid fell:\n" + "".join(map(chr, output)))


def part1(input_file):
  return run_springdroid(input_file, SCRIPT)


def main():
  input_file = "day21-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
