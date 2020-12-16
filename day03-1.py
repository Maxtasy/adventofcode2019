# https://adventofcode.com/2019/day/3


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    wire1 = []

    # lay out first wire
    cur_pos = [0, 0]
    instructions = lines[0].split(",")

    for instr in instructions:
      direction = instr[0]
      amount = int(instr[1:])

      for _ in range(amount):
        if direction == "U":
          cur_pos[0] -= 1
        elif direction == "D":
          cur_pos[0] += 1
        elif direction == "R":
          cur_pos[1] += 1
        elif direction == "L":
          cur_pos[1] -= 1

        wire1.append(cur_pos[:])

    # lay out second wire and check for intersections
    shortest_distance = 1e10
    cur_pos = [0, 0]

    instructions = lines[1].split(",")
    print(len(instructions))

    for i in range(len(instructions)):
      direction = instructions[i][0]
      amount = int(instructions[i][1:])

      for _ in range(amount):
        if direction == "U":
          cur_pos[0] -= 1
        elif direction == "D":
          cur_pos[0] += 1
        elif direction == "R":
          cur_pos[1] += 1
        elif direction == "L":
          cur_pos[1] -= 1
        
        if cur_pos in wire1:
          distance = abs(cur_pos[0]) + abs(cur_pos[1])
          shortest_distance = min(shortest_distance, distance)
          print("Found common coordinate", i, cur_pos, shortest_distance, len(wire1))

    return shortest_distance


def main():
  input_file = "day03-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()