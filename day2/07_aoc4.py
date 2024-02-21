# https://adventofcode.com/2023/day/4

# 4 Matches: 1 -> 2 -> 4 -> 8
import io

demo_input = io.StringIO("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""")

def card_value(scratchcard):
    _, numbers = scratchcard.split(':')
    winning_numbers, my_numbers = numbers.split('|')

    winning_numbers = set([int(x) for x in winning_numbers.split()])
    my_numbers = set([int(x) for x in my_numbers.split()])

    cross = winning_numbers.intersection(my_numbers)
    if len(cross) == 0:
        return 0
    else:
        return 2 ** (len(cross) - 1)


def part1(data):
    return sum(card_value(line) for line in data)



with open('aocday4.txt', encoding='utf8') as f:
    print(part1(f))

# print(part1(demo_input))



# find the sum(points_of_all_cards)