import string

digits = {
    digit_name: index + 1
    for index, digit_name in enumerate(['one',
                       'two',
                       'three',
                       'four',
                       'five',
                       'six',
                       'seven',
                       'eight',
                       'nine'])
} | { d: index + 1 for index, d in enumerate(string.digits[1:]) }

demo_input = ['1abc2',
              'pqr3stu8vwx',
              'a1b2c3d4e5f',
              'treb7uchet']

demo_input_2 = ['two1nine',     # 29
                'eightwothree', # 83
                'abcone2threexyz', # 13
                'xtwone3four', # 24
                '4nineeightseven2', #  42
                'zoneight234', # 14
                '7pqrstsixteen'] # 76

def to_list_of_digits(s: str) -> list[int]:
    result = []
    for ch in s:
        if ch.isdigit():
            result.append(int(ch))
    return result


def to_list_of_digits_2(s: str) -> list[int]:
    return [int(ch) for ch in s if ch.isdigit()]

# https://github.com/ynonp/perion-basic-python-2024-02
# https://adventofcode.com/2023/day/1

def fix_calibration_value(value: str) -> int:
    """
    Return a number made from the first digit in value
    concatenated with the last digit in value
    1abc2 => 12
    pqr3stu8vwx => 38
    a1b2c3d4e5f => 15
    treb7uchet => 77
    :param value:
    :return:
    """
    digits = to_list_of_digits_3(value)
    return (digits[0] * 10) + digits[-1]

def digits_at_index(calibration_value, index):
    for k in digits.keys():
        if calibration_value[index:index + len(k)] == k:
            return digits[k]
    return None

def to_list_of_digits_3(calibration_value):
    return [digits_at_index(calibration_value, i)
     for i in range(len(calibration_value))
     if digits_at_index(calibration_value, i) is not None]

# print(to_list_of_digits_3("abcone2threexyz"))

# print(sum([fix_calibration_value(s) for s in demo_input_2]))

with open('aocday1.txt', encoding='utf8') as f:
    print(sum([fix_calibration_value(line) for line in f]))








