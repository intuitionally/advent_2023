import math

def part1():
    with open('input_3.txt') as f:
        lines = f.readlines()
        lines = ['.' + x.strip() + '.' for x in lines]
        lines.insert(0, ''.ljust(len(lines[0]), '.'))
        lines.append(''.ljust(len(lines[0]), '.'))

        def part_number_adjacent(x, y):
            if not (lines[x-1][y-1].isdigit() or lines[x-1][y-1] == '.'):
                return True
            if not (lines[x][y-1].isdigit() or lines[x][y-1] == '.'):
                return True
            if not (lines[x+1][y-1].isdigit() or lines[x+1][y-1] == '.'):
                return True
            if not (lines[x-1][y].isdigit() or lines[x-1][y] == '.'):
                return True
            if not (lines[x+1][y].isdigit() or lines[x+1][y] == '.'):
                return True
            if not (lines[x-1][y+1].isdigit() or lines[x-1][y+1] == '.'):
                return True
            if not (lines[x][y+1].isdigit() or lines[x][y+1] == '.'):
                return True
            if not (lines[x+1][y+1].isdigit() or lines[x+1][y+1] == '.'):
                return True
            return False

        total = 0
        for row, line in enumerate(lines):
            current_num = ''
            start_index = 0
            for col, part in enumerate(line):
                if part.isdigit():
                    if current_num == '':
                        start_index = col
                    current_num += part
                elif not part.isdigit() and current_num != '':
                    for x in range(start_index, col):
                        if part_number_adjacent(row, x):
                            total += int(current_num)
                            current_num = ''
                            break
                    else:
                        current_num = ''
        print(total)


def part2():
    with open('input_3.txt') as f:
        lines = f.readlines()
        lines = ['.' + x.strip() + '.' for x in lines]
        lines.insert(0, ''.ljust(len(lines[0]), '.'))
        lines.append(''.ljust(len(lines[0]), '.'))

        gear_dict = {}

        def part_number_adjacent(x, y, current):
            if not (lines[x-1][y-1].isdigit() or lines[x-1][y-1] == '.') and lines[x-1][y-1] == '*':
                if (x-1, y-1) in gear_dict:
                    gear_dict[(x-1, y-1)].append(current)
                else:
                    gear_dict[(x - 1, y - 1)] = [current]
                return True
            if not (lines[x][y-1].isdigit() or lines[x][y-1] == '.') and lines[x][y-1] == '*':
                if (x, y-1) in gear_dict:
                    gear_dict[(x, y-1)].append(current)
                else:
                    gear_dict[(x, y - 1)] = [current]
                return True
            if not (lines[x+1][y-1].isdigit() or lines[x+1][y-1] == '.') and lines[x+1][y-1] == '*':
                if (x+1, y-1) in gear_dict:
                    gear_dict[(x+1, y-1)].append(current)
                else:
                    gear_dict[(x+1, y - 1)] = [current]
                return True
            if not (lines[x-1][y].isdigit() or lines[x-1][y] == '.') and lines[x-1][y] == '*':
                if (x-1, y) in gear_dict:
                    gear_dict[(x-1, y)].append(current)
                else:
                    gear_dict[(x-1, y)] = [current]
                return True
            if not (lines[x+1][y].isdigit() or lines[x+1][y] == '.') and lines[x+1][y] == '*':
                if (x+1, y) in gear_dict:
                    gear_dict[(x+1, y)].append(current)
                else:
                    gear_dict[(x+1, y)] = [current]
                return True
            if not (lines[x-1][y+1].isdigit() or lines[x-1][y+1] == '.') and lines[x-1][y+1] == '*':
                if (x-1, y+1) in gear_dict:
                    gear_dict[(x-1, y+1)].append(current)
                else:
                    gear_dict[(x-1, y+1)] = [current]
                return True
            if not (lines[x][y+1].isdigit() or lines[x][y+1] == '.') and lines[x][y+1] == '*':
                if (x, y+1) in gear_dict:
                    gear_dict[(x, y+1)].append(current)
                else:
                    gear_dict[(x, y+1)] = [current]
                return True
            if not (lines[x+1][y+1].isdigit() or lines[x+1][y+1] == '.') and lines[x+1][y+1] == '*':
                if (x+1, y+1) in gear_dict:
                    gear_dict[(x+1, y+1)].append(current)
                else:
                    gear_dict[(x+1, y+1)] = [current]
                return True
            return False

        total = 0

        for row, line in enumerate(lines):
            current_num = ''
            start_index = 0
            for col, part in enumerate(line):
                if part.isdigit():
                    if current_num == '':
                        start_index = col
                    current_num += part
                elif not part.isdigit() and current_num != '':
                    for x in range(start_index, col):
                        if part_number_adjacent(row, x, int(current_num)):
                            break
                    current_num = ''

        for gear in gear_dict.keys():
            if len(gear_dict[gear]) == 2:
                gear_dict[gear] = [int(x) for x in gear_dict[gear]]
                total += math.prod(gear_dict[gear])
        print(total)

part2()