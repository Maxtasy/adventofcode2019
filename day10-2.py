# https://adventofcode.com/2019/day/10
from math import atan2, gcd, pi

TARGET = 200


def load_asteroids(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")
  return [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line.strip()) if c == "#"]


def visible_count(station, asteroids):
  directions = set()
  for ax, ay in asteroids:
    if (ax, ay) == station:
      continue
    dx, dy = ax - station[0], ay - station[1]
    g = gcd(abs(dx), abs(dy))
    directions.add((dx // g, dy // g))
  return len(directions)


def part2(input_file):
  asteroids = load_asteroids(input_file)
  station = max(asteroids, key=lambda a: visible_count(a, asteroids))

  # group by direction, closest first
  by_direction = {}
  for ax, ay in asteroids:
    if (ax, ay) == station:
      continue
    dx, dy = ax - station[0], ay - station[1]
    # angle clockwise from "up" (negative y)
    angle = atan2(dx, -dy)
    if angle < 0:
      angle += 2 * pi
    by_direction.setdefault(angle, []).append((abs(dx) + abs(dy), ax, ay))

  queues = [sorted(by_direction[a]) for a in sorted(by_direction)]

  count = 0
  while True:
    for queue in queues:
      if queue:
        _, x, y = queue.pop(0)
        count += 1
        if count == TARGET:
          return x * 100 + y


def main():
  input_file = "day10-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
