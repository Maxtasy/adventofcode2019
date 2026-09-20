# https://adventofcode.com/2019/day/24
from collections import Counter

MINUTES = 200


def neighbours(x, y, level):
  result = []
  for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    nx, ny = x + dx, y + dy
    if nx < 0:
      result.append((1, 2, level - 1))
    elif nx > 4:
      result.append((3, 2, level - 1))
    elif ny < 0:
      result.append((2, 1, level - 1))
    elif ny > 4:
      result.append((2, 3, level - 1))
    elif (nx, ny) == (2, 2):
      # stepping into the centre tile leads into the inner level
      if dx == 1:
        result.extend((0, i, level + 1) for i in range(5))
      elif dx == -1:
        result.extend((4, i, level + 1) for i in range(5))
      elif dy == 1:
        result.extend((i, 0, level + 1) for i in range(5))
      else:
        result.extend((i, 4, level + 1) for i in range(5))
    else:
      result.append((nx, ny, level))
  return result


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  bugs = {(x, y, 0) for y, line in enumerate(lines) for x, c in enumerate(line.strip()) if c == "#" and (x, y) != (2, 2)}

  for _ in range(MINUTES):
    counts = Counter()
    for x, y, level in bugs:
      for n in neighbours(x, y, level):
        counts[n] += 1

    bugs = {pos for pos, n in counts.items() if n == 1 or (n == 2 and pos not in bugs)}

  return len(bugs)


def main():
  input_file = "day24-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
