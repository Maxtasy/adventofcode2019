# https://adventofcode.com/2019/day/3


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    wire1 = {}

    # lay out first wire
    cur_pos = [0, 0]
    instructions = lines[0].split(",")
    steps = 0

    for instr in instructions:
      direction = instr[0]
      amount = int(instr[1:])

      for j in range(amount):
        if direction == "U":
          cur_pos[0] -= 1
        elif direction == "D":
          cur_pos[0] += 1
        elif direction == "R":
          cur_pos[1] += 1
        elif direction == "L":
          cur_pos[1] -= 1
        
        steps += 1

        if not wire1.get((cur_pos[0], cur_pos[1])):
          wire1[(cur_pos[0], cur_pos[1])] = steps

    # lay out second wire and check for intersections
    combined_steps = 1e10

    cur_pos = [0, 0]
    instructions = lines[1].split(",")
    steps = 0

    for instr in instructions:
      direction = instr[0]
      amount = int(instr[1:])

      for j in range(amount):
        if direction == "U":
          cur_pos[0] -= 1
        elif direction == "D":
          cur_pos[0] += 1
        elif direction == "R":
          cur_pos[1] += 1
        elif direction == "L":
          cur_pos[1] -= 1
        
        steps += 1
        
        if (cur_pos[0], cur_pos[1]) in wire1.keys():
          combined_steps = min(combined_steps, wire1[(cur_pos[0], cur_pos[1])] + steps)
          print("Found common coordinate", cur_pos, combined_steps)

    return combined_steps


def main():
  input_file = "day03-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()