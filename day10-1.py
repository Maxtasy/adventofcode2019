# https://adventofcode.com/2019/day/10
from math import gcd


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


def part1(input_file):
  asteroids = load_asteroids(input_file)
  return max(visible_count(a, asteroids) for a in asteroids)


def main():
  input_file = "day10-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
