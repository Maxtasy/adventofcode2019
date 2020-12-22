# https://adventofcode.com/2019/day/4


def part2(input_file):
  with open(input_file, "r") as f:
    range_min, range_max = list(map(int, f.read().strip().split("-")))

    possibles_passwords = []

    for i in range(range_min, range_max + 1):
      hasExclusivePair = False
      ordered = True

      num_str = str(i)
      for j in range(len(num_str)-1):
        if num_str[j] == num_str[j+1]:
          if j > 0 and num_str[j] == num_str[j-1]:
            continue
          elif j < len(num_str) - 2 and num_str[j] == num_str[j+2]:
            continue

          hasExclusivePair = True
        elif num_str[j] > num_str[j+1]:
          ordered = False
          break
      
      possible = hasExclusivePair and ordered

      if possible:
        possibles_passwords.append(i)
    
    return len(possibles_passwords)


def main():
  input_file = "day04-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()