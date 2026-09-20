# https://adventofcode.com/2019/day/16

PHASES = 100
REPEATS = 10000


def part2(input_file):
  with open(input_file, "r") as f:
    signal = f.read().strip()

  offset = int(signal[:7])
  total_len = len(signal) * REPEATS
  # The offset lies in the second half, where every output digit is the suffix sum of the input digits.
  assert offset >= total_len // 2

  digits = list(map(int, (signal * REPEATS)[offset:]))
  for _ in range(PHASES):
    running = 0
    for i in range(len(digits) - 1, -1, -1):
      running = (running + digits[i]) % 10
      digits[i] = running

  return "".join(map(str, digits[:8]))


def main():
  input_file = "day16-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
