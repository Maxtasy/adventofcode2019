# https://adventofcode.com/2019/day/20
from collections import deque


def load_maze(input_file):
  # leading whitespace is significant here, so only strip newlines
  with open(input_file, "r") as f:
    lines = f.read().split("\n")
  lines = [l for l in lines if l.strip()]
  width = max(len(l) for l in lines)
  return [l.ljust(width) for l in lines]


def find_portals(grid):
  # Returns (start, end, links) where links maps a tile to (other tile, level change).
  height, width = len(grid), len(grid[0])
  labels = {}

  for y in range(height):
    for x in range(width):
      if grid[y][x] != ".":
        continue
      for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        c1 = grid[y + dy][x + dx] if 0 <= y + dy < height and 0 <= x + dx < width else " "
        if not c1.isupper():
          continue
        c2 = grid[y + 2 * dy][x + 2 * dx]
        label = c1 + c2 if (dx, dy) in ((1, 0), (0, 1)) else c2 + c1
        outer = x <= 2 or y <= 2 or x >= width - 3 or y >= height - 3
        labels.setdefault(label, []).append(((x, y), outer))

  links = {}
  for label, ends in labels.items():
    if len(ends) == 2:
      (a, a_outer), (b, b_outer) = ends
      links[a] = (b, -1 if a_outer else 1)
      links[b] = (a, -1 if b_outer else 1)

  return labels["AA"][0][0], labels["ZZ"][0][0], links


def shortest(grid, recursive):
  start, end, links = find_portals(grid)
  queue = deque([(start, 0, 0)])
  seen = {(start, 0)}

  while queue:
    (x, y), level, dist = queue.popleft()
    if (x, y) == end and level == 0:
      return dist

    neighbours = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      if grid[y + dy][x + dx] == ".":
        neighbours.append(((x + dx, y + dy), level))
    if (x, y) in links:
      other, change = links[(x, y)]
      new_level = level + change if recursive else 0
      if new_level >= 0:
        neighbours.append((other, new_level))

    for pos, lvl in neighbours:
      if (pos, lvl) not in seen:
        seen.add((pos, lvl))
        queue.append((pos, lvl, dist + 1))


def part1(input_file):
  return shortest(load_maze(input_file), False)


def main():
  input_file = "day20-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
