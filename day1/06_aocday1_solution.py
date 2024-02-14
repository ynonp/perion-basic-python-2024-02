demo_input = ['1abc2',
              'pqr3stu8vwx',
              'a1b2c3d4e5f'
              'treb7uchet']

demo_input_2 = ['two1nine',     # 29
                'eightwothree', # 83
                'abcone2threexyz', # 13
                'xtwone3four', # 24
                '4nineeightseven2', #  42
                'zoneight234', # 14
                '7pqrstsixteen'] # 76

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
    ...
