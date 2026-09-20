# https://adventofcode.com/2019/day/18
import heapq
from collections import deque


def load_grid(input_file):
  with open(input_file, "r") as f:
    return [list(line) for line in f.read().strip().split("\n")]


def reachable_keys(grid, start):
  # BFS from start; returns {key: (distance, doors_needed_bitmask)}
  result = {}
  seen = {start}
  queue = deque([(start, 0, 0)])
  while queue:
    (x, y), dist, doors = queue.popleft()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      nx, ny = x + dx, y + dy
      if (nx, ny) in seen or grid[ny][nx] == "#":
        continue
      seen.add((nx, ny))
      c = grid[ny][nx]
      ndoors = doors
      if c.isupper():
        ndoors |= 1 << (ord(c) - ord("A"))
      elif c.islower():
        result[c] = (dist + 1, doors)
      queue.append(((nx, ny), dist + 1, ndoors))
  return result


def solve(grid):
  starts = [(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "@"]
  keys = {c: (x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c.islower()}
  all_keys = (1 << len(keys)) - 1

  # graph: node -> {key: (dist, doors)}, nodes are start indices ("@0", ...) and keys
  graph = {}
  for i, s in enumerate(starts):
    graph["@%d" % i] = reachable_keys(grid, s)
  for k, pos in keys.items():
    graph[k] = reachable_keys(grid, pos)

  start_state = (0, tuple("@%d" % i for i in range(len(starts))), 0)
  best = {(start_state[1], 0): 0}
  heap = [start_state]

  while heap:
    dist, nodes, collected = heapq.heappop(heap)
    if collected == all_keys:
      return dist
    if best.get((nodes, collected), 1e18) < dist:
      continue
    for i, node in enumerate(nodes):
      for key, (d, doors) in graph[node].items():
        bit = 1 << (ord(key) - ord("a"))
        if collected & bit or doors & ~collected:
          continue
        new_nodes = nodes[:i] + (key,) + nodes[i + 1:]
        state = (new_nodes, collected | bit)
        nd = dist + d
        if nd < best.get(state, 1e18):
          best[state] = nd
          heapq.heappush(heap, (nd, new_nodes, collected | bit))


def part1(input_file):
  return solve(load_grid(input_file))


def main():
  input_file = "day18-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
