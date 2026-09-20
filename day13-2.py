# https://adventofcode.com/2019/day/13
from intcode import Intcode, load_program


def part2(input_file):
  program = load_program(input_file)
  program[0] = 2  # insert quarters
  game = Intcode(program)

  score = 0
  ball_x = 0
  paddle_x = 0
  consumed = 0

  while True:
    running = game.run()
    # process any new complete output triples
    while len(game.outputs) - consumed >= 3:
      x, y, tile = game.outputs[consumed:consumed + 3]
      consumed += 3
      if x == -1 and y == 0:
        score = tile
      elif tile == 3:
        paddle_x = x
      elif tile == 4:
        ball_x = x

    if running is None:
      break
    if running is False:
      # joystick: follow the ball with the paddle
      game.inputs.append((ball_x > paddle_x) - (ball_x < paddle_x))

  return score


def main():
  input_file = "day13-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
