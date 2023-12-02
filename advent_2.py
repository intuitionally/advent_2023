import math


def part1():
    with open('input_2.txt') as f:
        lines = f.readlines()
        color_dict = {'red': 12, 'green': 13, 'blue': 14}
        total = 0
        for line in lines:
            line = line.strip()
            game_num = int(line.split(':')[0].split(' ')[1])
            games = set(line.split(': ')[1].split('; '))
            for game in games:
                game = set([(x.split(' ')[0], x.split(' ')[1]) for x in game.split(', ')])
                bad = True
                for color in game:
                    if int(color[0]) > color_dict[color[1]]:
                        break
                else:
                    bad = False
                if bad:
                    break
            else:
                total += game_num
        print(total)


def part2():
    with open('input_2.txt') as f:
        lines = f.readlines()
        color_dict = {'red': 0, 'green': 0, 'blue': 0}
        total = 0
        for line in lines:
            line = line.strip()
            games = set(line.split(': ')[1].split('; '))
            for game in games:
                game = set([(x.split(' ')[0], x.split(' ')[1]) for x in game.split(', ')])
                for color in game:
                    if int(color[0]) > color_dict[color[1]]:
                        color_dict[color[1]] = int(color[0])
            total += math.prod(color_dict.values())
            color_dict = dict.fromkeys(color_dict, 0)
        print(total)


part2()
