import re

def generator_numbers(text):
    numbers_pattern = r'\b\d+(\.\d+)?\b'
    for match in re.finditer(numbers_pattern, text):
        yield float(match.group())

def sum_profit(text, func):
    total = 0
    for number in func(text):
        total += number
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") 