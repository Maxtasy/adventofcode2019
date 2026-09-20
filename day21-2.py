# https://adventofcode.com/2019/day/21
import importlib

day21 = importlib.import_module("day21-1")

# Same as part 1, but only jump if we can also either walk (E) or jump again (H) after landing on D.
SCRIPT = [
  "NOT A J",
  "NOT B T",
  "OR T J",
  "NOT C T",
  "OR T J",
  "AND D J",
  "NOT E T",
  "NOT T T",
  "OR H T",
  "AND T J",
  "RUN",
]


def part2(input_file):
  return day21.run_springdroid(input_file, SCRIPT)


def main():
  input_file = "day21-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
