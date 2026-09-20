# https://adventofcode.com/2019/day/12
import re
from math import gcd


def axis_period(start_pos):
  pos = start_pos[:]
  vel = [0] * len(pos)
  initial = (tuple(pos), tuple(vel))
  steps = 0

  while True:
    for i in range(len(pos)):
      for j in range(len(pos)):
        if pos[j] > pos[i]:
          vel[i] += 1
        elif pos[j] < pos[i]:
          vel[i] -= 1
    for i in range(len(pos)):
      pos[i] += vel[i]
    steps += 1
    if (tuple(pos), tuple(vel)) == initial:
      return steps


def part2(input_file):
  with open(input_file, "r") as f:
    moons = [list(map(int, re.findall(r"-?\d+", line))) for line in f.read().strip().split("\n")]

  result = 1
  for k in range(3):
    period = axis_period([m[k] for m in moons])
    result = result * period // gcd(result, period)
  return result


def main():
  input_file = "day12-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
