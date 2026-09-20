# https://adventofcode.com/2019/day/23
from intcode import Intcode, load_program

COMPUTERS = 50


def run_network(program, use_nat):
  computers = [Intcode(program, [i]) for i in range(COMPUTERS)]
  queues = [[] for _ in range(COMPUTERS)]
  nat = None
  last_nat_y = None

  while True:
    idle = True
    for i, comp in enumerate(computers):
      comp.inputs.extend(queues[i] if queues[i] else [-1])
      if queues[i]:
        idle = False
      queues[i] = []

      # run until the computer waits for input again, collecting packets
      while comp.run():
        if len(comp.outputs) >= 3:
          dest, x, y = comp.outputs[:3]
          del comp.outputs[:3]
          idle = False
          if dest == 255:
            if not use_nat:
              return y
            nat = (x, y)
          else:
            queues[dest].extend([x, y])

    if use_nat and idle and nat:
      if nat[1] == last_nat_y:
        return nat[1]
      last_nat_y = nat[1]
      queues[0].extend(nat)


def part1(input_file):
  return run_network(load_program(input_file), False)


def main():
  input_file = "day23-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
