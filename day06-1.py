# https://adventofcode.com/2019/day/6


def part1(input_file):
  with open(input_file, "r") as f:
    parent = {}
    for line in f.read().strip().split("\n"):
      center, obj = line.strip().split(")")
      parent[obj] = center

    depth = {"COM": 0}

    def get_depth(obj):
      if obj not in depth:
        depth[obj] = get_depth(parent[obj]) + 1
      return depth[obj]

    return sum(get_depth(obj) for obj in parent)


def main():
  input_file = "day06-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
