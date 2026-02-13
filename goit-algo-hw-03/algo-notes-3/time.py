import time

current_time = time.time()
print(f"Поточний час: {current_time}")

def second() -> int:
    n = 0
    while n < 100:
        n += 1
        print('-', end='')
    print('-')    
    return 3    

def time_sleep():
    while time.sleep(2):
        print('-', end='')

print("Початок паузи")
# time.sleep(3)
time_sleep()
# time.sleep(second())
print("Кінець паузи")


current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

gm_time = time.gmtime(current_time)
print(f"Гринвічський час: {gm_time}")


# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")