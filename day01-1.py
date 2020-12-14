# https://adventofcode.com/2019/day/1


def part1(input_file):
	with open(input_file, "r") as f:
		masses = list(map(int, f.read().strip().split("\n")))

		fuels = []

		for mass in masses:
			fuels.append(mass//3-2)

		return sum(fuels)


def main():
	input_file = "day01-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()