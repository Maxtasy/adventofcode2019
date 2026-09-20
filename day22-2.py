# https://adventofcode.com/2019/day/22

DECK_SIZE = 119315717514047
SHUFFLES = 101741582076661
POSITION = 2020


def part2(input_file):
  with open(input_file, "r") as f:
    instructions = f.read().strip().split("\n")

  # One shuffle maps position p to (a * p + b) % DECK_SIZE.
  a, b = 1, 0
  for line in instructions:
    if line.startswith("deal into new stack"):
      a, b = -a, -b - 1
    elif line.startswith("cut"):
      b -= int(line.split()[-1])
    elif line.startswith("deal with increment"):
      n = int(line.split()[-1])
      a, b = a * n, b * n
    a %= DECK_SIZE
    b %= DECK_SIZE

  # Apply it SHUFFLES times: f^k(p) = a^k * p + b * (a^k - 1) / (a - 1)
  ak = pow(a, SHUFFLES, DECK_SIZE)
  bk = b * (ak - 1) * pow(a - 1, -1, DECK_SIZE) % DECK_SIZE

  # Find the card that ends up at POSITION: solve ak * card + bk = POSITION
  return (POSITION - bk) * pow(ak, -1, DECK_SIZE) % DECK_SIZE


def main():
  input_file = "day22-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
