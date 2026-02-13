def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55
print(fibonacci(0))  # виведе 0
print(fibonacci(1))  # виведе 1