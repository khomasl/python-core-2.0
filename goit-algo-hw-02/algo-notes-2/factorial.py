def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n - 1) # рекурсивний випадок
    
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1

def factorial_(n):
    return 1 if n==0 else n * factorial_(n - 1) # рекурсивний випадок

print(factorial_(5))  # Output: 120
print(factorial_(0))  # Output: 1