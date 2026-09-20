# https://adventofcode.com/2019/day/12
import re

STEPS = 1000


def part1(input_file):
  with open(input_file, "r") as f:
    pos = [list(map(int, re.findall(r"-?\d+", line))) for line in f.read().strip().split("\n")]
  vel = [[0, 0, 0] for _ in pos]

  for _ in range(STEPS):
    for i in range(len(pos)):
      for j in range(len(pos)):
        for k in range(3):
          if pos[j][k] > pos[i][k]:
            vel[i][k] += 1
          elif pos[j][k] < pos[i][k]:
            vel[i][k] -= 1
    for i in range(len(pos)):
      for k in range(3):
        pos[i][k] += vel[i][k]

  return sum(sum(map(abs, p)) * sum(map(abs, v)) for p, v in zip(pos, vel))


def main():
  input_file = "day12-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
