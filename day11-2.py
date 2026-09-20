# https://adventofcode.com/2019/day/11
from intcode import Intcode, load_program


def paint(program, start_color):
  robot = Intcode(program)
  panels = {(0, 0): start_color}
  x, y = 0, 0
  dx, dy = 0, -1

  while True:
    robot.inputs.append(panels.get((x, y), 0))
    color = robot.step_output()
    if color is None:
      break
    turn = robot.step_output()
    if turn is None:
      break

    panels[(x, y)] = color
    dx, dy = (dy, -dx) if turn == 0 else (-dy, dx)  # 0 = left, 1 = right
    x, y = x + dx, y + dy

  return panels


def part2(input_file):
  panels = paint(load_program(input_file), 1)
  white = [p for p, c in panels.items() if c == 1]
  min_x, max_x = min(p[0] for p in white), max(p[0] for p in white)
  min_y, max_y = min(p[1] for p in white), max(p[1] for p in white)

  rows = []
  for y in range(min_y, max_y + 1):
    rows.append("".join("#" if panels.get((x, y)) == 1 else " " for x in range(min_x, max_x + 1)))
  return "\n".join(rows)


def main():
  input_file = "day11-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
