import re
from typing import Callable, Iterable


def generator_numbers(text: str):
    pattern = r"\d+\.\d+|\d+"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable[[str], Iterable]):
    return sum(func(text))
