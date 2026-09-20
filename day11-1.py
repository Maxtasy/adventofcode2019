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


def part1(input_file):
  return len(paint(load_program(input_file), 0))


def main():
  input_file = "day11-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
