def divide(a, b):
    return a / b

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def is_even(n):
    return n % 2 == 0