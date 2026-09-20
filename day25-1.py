# https://adventofcode.com/2019/day/25
import re
from itertools import combinations
from intcode import Intcode, load_program

# Items that end the game or freeze the droid when picked up.
DANGEROUS = {"infinite loop", "giant electromagnet", "molten lava", "escape pod", "photons"}
OPPOSITE = {"north": "south", "south": "north", "east": "west", "west": "east"}


class Game:
  def __init__(self, program):
    self.droid = Intcode(program)
    self.text = self.read()

  def read(self):
    self.droid.outputs = []
    self.droid.run_all()
    return "".join(map(chr, self.droid.outputs))

  def send(self, command):
    self.droid.inputs.extend(ord(c) for c in command + "\n")
    self.text = self.read()
    return self.text


def parse_room(text):
  name = re.findall(r"== (.+) ==", text)[-1]
  doors_part = text.split("Doors here lead:")[1].split("\n\n")[0]
  doors = re.findall(r"- (\w+)", doors_part)
  items = []
  if "Items here:" in text:
    items = re.findall(r"- (.+)", text.split("Items here:")[1].split("\n\n")[0])
  return name, doors, items


def explore(game):
  # Collect every safe item and remember how to reach the Security Checkpoint.
  inventory = []
  checkpoint = {}
  visited = set()

  def dfs(text, path):
    name, doors, items = parse_room(text)
    visited.add(name)
    for item in items:
      if item not in DANGEROUS:
        game.send("take " + item)
        inventory.append(item)

    if name == "Security Checkpoint":
      checkpoint["path"] = path[:]
      return

    for door in doors:
      # the door back where we came from is always explored last / skipped by the visited check
      new_text = game.send(door)
      new_name = parse_room(new_text)[0]
      if new_name in visited:
        game.send(OPPOSITE[door])
        continue
      dfs(new_text, path + [door])
      game.send(OPPOSITE[door])

  dfs(game.text, [])
  return inventory, checkpoint["path"]


def part1(input_file):
  game = Game(load_program(input_file))
  inventory, path = explore(game)

  # walk to the Security Checkpoint (the game state is currently back in the starting room)
  for door in path:
    game.send(door)
  # the checkpoint's unexplored door is the one that leads to the pressure-sensitive floor
  _, doors, _ = parse_room(game.text)
  final_door = next(d for d in doors if d != OPPOSITE[path[-1]])

  held = set(inventory)
  for size in range(len(inventory) + 1):
    for subset in combinations(inventory, size):
      for item in held - set(subset):
        game.send("drop " + item)
      for item in set(subset) - held:
        game.send("take " + item)
      held = set(subset)

      result = game.send(final_door)
      match = re.search(r"typing (\d+) on the keypad", result)
      if match:
        return int(match.group(1))


def main():
  input_file = "day25-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
