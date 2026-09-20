# https://adventofcode.com/2019/day/8
WIDTH = 25
HEIGHT = 6


def part2(input_file):
  with open(input_file, "r") as f:
    data = f.read().strip()
    size = WIDTH * HEIGHT
    layers = [data[i:i+size] for i in range(0, len(data), size)]

    rows = []
    for y in range(HEIGHT):
      row = ""
      for x in range(WIDTH):
        pixel = next(l[y * WIDTH + x] for l in layers if l[y * WIDTH + x] != "2")
        row += "#" if pixel == "1" else " "
      rows.append(row)

    return "\n".join(rows)


def main():
  input_file = "day08-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
