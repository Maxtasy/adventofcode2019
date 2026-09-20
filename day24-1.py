# https://adventofcode.com/2019/day/24


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  bugs = frozenset((x, y) for y, line in enumerate(lines) for x, c in enumerate(line.strip()) if c == "#")
  seen = {bugs}

  while True:
    new_bugs = set()
    for y in range(5):
      for x in range(5):
        n = sum((x + dx, y + dy) in bugs for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        if (x, y) in bugs:
          if n == 1:
            new_bugs.add((x, y))
        elif n in (1, 2):
          new_bugs.add((x, y))

    bugs = frozenset(new_bugs)
    if bugs in seen:
      return sum(2 ** (y * 5 + x) for x, y in bugs)
    seen.add(bugs)


def main():
  input_file = "day24-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
