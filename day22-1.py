# https://adventofcode.com/2019/day/22

DECK_SIZE = 10007
CARD = 2019


def part1(input_file):
  with open(input_file, "r") as f:
    instructions = f.read().strip().split("\n")

  pos = CARD
  for line in instructions:
    if line.startswith("deal into new stack"):
      pos = DECK_SIZE - 1 - pos
    elif line.startswith("cut"):
      pos = (pos - int(line.split()[-1])) % DECK_SIZE
    elif line.startswith("deal with increment"):
      pos = (pos * int(line.split()[-1])) % DECK_SIZE

  return pos


def main():
  input_file = "day22-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
