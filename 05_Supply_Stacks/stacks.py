import re
from collections import deque


def parse_stacks(input_lines:list):
    input_lines.reverse()
    numbers = re.findall('[0-9]',input_lines[0])
    stacks = {}
    for num in numbers:
        stacks.update({int(num): deque()})


    for line in input_lines[1:]:
        for idx, container in enumerate(re.findall('\[[A-Z]\]| {4}', line)):
            if "   " in container:
                continue
            else:
                stacks[idx+1].append(container)

    return stacks

def print_stacks(stacks):
    for number in stacks.keys():
        line = f"{number}: "
        for container in stacks[number]:
            line += container + " "

        print(line)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        idx = lines.index("\n")
        stacks = parse_stacks(lines[:idx])
        print("Starting state")
        print_stacks(stacks)
        
        for moves in lines[idx+1:]:
            numbers = re.findall('[0-9]+',moves)
            temp = []
            for _ in range(int(numbers[0])):
                temp.append(stacks[int(numbers[1])].pop())

            temp.reverse()
            for item in temp:
                stacks[int(numbers[2])].append(item)

        print("\n\nEnd state")
        print_stacks(stacks)

