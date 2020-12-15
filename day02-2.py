# https://adventofcode.com/2019/day/2


TARGET_OUTPUT = 19690720


def part2(input_file):
  with open(input_file, "r") as f:
    numbers = list(map(int, f.read().strip().split(",")))

    noun = None
    verb = None

    found = False

    for i in range(100):
      for j in range(100):
        numbers_copy = numbers[:]

        numbers_copy[1] = i
        numbers_copy[2] = j

        index = 0

        while index <= len(numbers_copy) - 4:
          opcode = numbers_copy[index]
          pos1 = numbers_copy[index+1]
          pos2 = numbers_copy[index+2]
          pos3 = numbers_copy[index+3]

          if opcode == 1:
            numbers_copy[pos3] = numbers_copy[pos1] + numbers_copy[pos2]
          elif opcode == 2:
            numbers_copy[pos3] = numbers_copy[pos1] * numbers_copy[pos2]
          elif opcode == 99:
            break
          
          index += 4
        
        if numbers_copy[0] == TARGET_OUTPUT:
          found = True
          noun = i
          verb = j
          break
      
      if found:
        break
    
    return 100 * noun + verb


def main():
  input_file = "day02-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()