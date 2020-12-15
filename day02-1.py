# https://adventofcode.com/2019/day/2


def part1(input_file):
  with open(input_file, "r") as f:
    numbers = list(map(int, f.read().strip().split(",")))

    numbers[1] = 12
    numbers[2] = 2

    index = 0

    while index <= len(numbers) - 4:
      opcode = numbers[index]
      pos1 = numbers[index+1]
      pos2 = numbers[index+2]
      pos3 = numbers[index+3]

      if opcode == 1:
        numbers[pos3] = numbers[pos1] + numbers[pos2]
      elif opcode == 2:
        numbers[pos3] = numbers[pos1] * numbers[pos2]
      elif opcode == 99:
        break
      
      index += 4
    
    return numbers[0]


def main():
  input_file = "day02-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()