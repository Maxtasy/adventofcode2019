# https://adventofcode.com/2019/day/15
import sys
from collections import deque
from intcode import Intcode, load_program

# movement command -> (dx, dy), opposite command
MOVES = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
OPPOSITE = {1: 2, 2: 1, 3: 4, 4: 3}


def explore(program):
  # Depth-first exploration with backtracking; returns the map {(x, y): tile} and the oxygen system position.
  droid = Intcode(program)
  grid = {(0, 0): 1}
  oxygen = None
  sys.setrecursionlimit(10000)

  def move(cmd):
    droid.inputs.append(cmd)
    return droid.step_output()

  def dfs(x, y):
    nonlocal oxygen
    for cmd, (dx, dy) in MOVES.items():
      nx, ny = x + dx, y + dy
      if (nx, ny) in grid:
        continue
      status = move(cmd)
      grid[(nx, ny)] = status
      if status == 0:
        continue
      if status == 2:
        oxygen = (nx, ny)
      dfs(nx, ny)
      move(OPPOSITE[cmd])

  dfs(0, 0)
  return grid, oxygen


def bfs(grid, start):
  dist = {start: 0}
  queue = deque([start])
  while queue:
    x, y = queue.popleft()
    for dx, dy in MOVES.values():
      n = (x + dx, y + dy)
      if grid.get(n, 0) != 0 and n not in dist:
        dist[n] = dist[(x, y)] + 1
        queue.append(n)
  return dist


def part1(input_file):
  grid, oxygen = explore(load_program(input_file))
  return bfs(grid, (0, 0))[oxygen]


def main():
  input_file = "day15-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
