import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if quantity > (max - min + 1) or min < 0 or max > 1000:
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)
    
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 10, 0)
print("Ваші лотерейні числа:", lottery_numbers)