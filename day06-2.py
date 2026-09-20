# https://adventofcode.com/2019/day/6


def path_to_com(parent, obj):
  path = []
  while obj in parent:
    obj = parent[obj]
    path.append(obj)
  return path


def part2(input_file):
  with open(input_file, "r") as f:
    parent = {}
    for line in f.read().strip().split("\n"):
      center, obj = line.strip().split(")")
      parent[obj] = center

    you = path_to_com(parent, "YOU")
    san = path_to_com(parent, "SAN")
    san_set = set(san)

    for i, obj in enumerate(you):
      if obj in san_set:
        return i + san.index(obj)


def main():
  input_file = "day06-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
