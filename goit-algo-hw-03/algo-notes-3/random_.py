import random

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Перемішана колода: {cards}")

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, weights=[0.1, 0.5, 0.2, 0.2], k=3)
print(chosen_item)  

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")