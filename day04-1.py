# https://adventofcode.com/2019/day/4


def part1(input_file):
  with open(input_file, "r") as f:
    range_min, range_max = list(map(int, f.read().strip().split("-")))

    possibles_passwords = []

    for i in range(range_min, range_max + 1):
      hasPair = False
      ordered = True

      num_str = str(i)
      for j in range(len(num_str)-1):
        if num_str[j] == num_str[j+1]:
          hasPair = True
        elif num_str[j] > num_str[j+1]:
          ordered = False
          break
      
      possible = hasPair and ordered

      if possible:
        possibles_passwords.append(i)
    
    return len(possibles_passwords)


def main():
  input_file = "day04-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()