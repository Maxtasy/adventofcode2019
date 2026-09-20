# https://adventofcode.com/2019/day/16

PHASES = 100
BASE_PATTERN = [0, 1, 0, -1]


def part1(input_file):
  with open(input_file, "r") as f:
    digits = list(map(int, f.read().strip()))

  n = len(digits)
  for _ in range(PHASES):
    new_digits = []
    for i in range(n):
      total = 0
      for j in range(i, n):
        total += digits[j] * BASE_PATTERN[((j + 1) // (i + 1)) % 4]
      new_digits.append(abs(total) % 10)
    digits = new_digits

  return "".join(map(str, digits[:8]))


def main():
  input_file = "day16-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
