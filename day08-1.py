# https://adventofcode.com/2019/day/8
WIDTH = 25
HEIGHT = 6


def part1(input_file):
  with open(input_file, "r") as f:
    data = f.read().strip()
    size = WIDTH * HEIGHT
    layers = [data[i:i+size] for i in range(0, len(data), size)]
    layer = min(layers, key=lambda l: l.count("0"))
    return layer.count("1") * layer.count("2")


def main():
  input_file = "day08-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
