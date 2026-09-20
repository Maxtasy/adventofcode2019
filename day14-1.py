# https://adventofcode.com/2019/day/14
import re
from collections import defaultdict


def parse(input_file):
  reactions = {}
  with open(input_file, "r") as f:
    for line in f.read().strip().split("\n"):
      left, right = line.split("=>")
      amount, name = right.split()
      inputs = [(int(a), n) for a, n in re.findall(r"(\d+) (\w+)", left)]
      reactions[name] = (int(amount), inputs)
  return reactions


def ore_for_fuel(reactions, fuel):
  needed = defaultdict(int)
  needed["FUEL"] = fuel
  leftover = defaultdict(int)
  ore = 0

  queue = ["FUEL"]
  while queue:
    chem = queue.pop()
    amount = needed.pop(chem, 0)
    if amount == 0:
      continue
    if chem == "ORE":
      ore += amount
      continue

    use = min(amount, leftover[chem])
    leftover[chem] -= use
    amount -= use
    if amount == 0:
      continue

    produced, inputs = reactions[chem]
    times = -(-amount // produced)
    leftover[chem] += times * produced - amount
    for a, n in inputs:
      needed[n] += a * times
      queue.append(n)

  return ore


def part1(input_file):
  return ore_for_fuel(parse(input_file), 1)


def main():
  input_file = "day14-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
