# https://adventofcode.com/2019/day/17
from intcode import Intcode, load_program


def get_grid(program):
  output = Intcode(program).run_all()
  return "".join(map(chr, output)).strip().split("\n")


def trace_path(grid):
  # Walk the scaffold straight ahead as far as possible, turning only at the ends.
  height = len(grid)

  def at(x, y):
    return grid[y][x] if 0 <= y < height and 0 <= x < len(grid[y]) else "."

  x, y, dx, dy = next((x, y, {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}[c][0],
                       {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}[c][1])
                      for y, row in enumerate(grid) for x, c in enumerate(row) if c in "^v<>")

  path = []
  while True:
    for turn, (ndx, ndy) in (("L", (dy, -dx)), ("R", (-dy, dx))):
      if at(x + ndx, y + ndy) == "#":
        dx, dy = ndx, ndy
        break
    else:
      return path

    steps = 0
    while at(x + dx, y + dy) == "#":
      x, y = x + dx, y + dy
      steps += 1
    path.append(turn)
    path.append(str(steps))


def compress(path):
  # Find main routine + functions A, B, C (each at most 20 characters when comma separated).
  def fits(tokens):
    return len(",".join(tokens)) <= 20

  def solve(remaining, funcs):
    if not remaining:
      return [], funcs
    # try existing functions
    for name, body in zip("ABC", funcs):
      if remaining[:len(body)] == body:
        result = solve(remaining[len(body):], funcs)
        if result:
          return [name] + result[0], result[1]
    if len(funcs) < 3:
      for length in range(1, len(remaining) + 1):
        body = remaining[:length]
        if not fits(body):
          break
        result = solve(remaining[length:], funcs + [body])
        if result:
          return ["ABC"[len(funcs)]] + result[0], result[1]
    return None

  routine, funcs = solve(path, [])
  assert fits(routine)
  return routine, funcs


def part2(input_file):
  program = load_program(input_file)
  path = trace_path(get_grid(program))
  routine, funcs = compress(path)

  lines = [",".join(routine)] + [",".join(f) for f in funcs] + ["n"]
  while len(lines) < 5:
    lines.insert(-1, "")
  text = "\n".join(lines) + "\n"

  program[0] = 2
  robot = Intcode(program, [ord(c) for c in text])
  return robot.run_all()[-1]


def main():
  input_file = "day17-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
