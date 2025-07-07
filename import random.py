import random

def get_numbers_ticket(min_num, max_num, quantity):
    if (
        not isinstance(min_num, int) or
        not isinstance(max_num, int) or
        not isinstance(quantity, int)
    ):
        return []

    if min_num < 1 or max_num > 1000 or min_num > max_num:
        return []

    if quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)

    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
