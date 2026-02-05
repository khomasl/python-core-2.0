def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

print(number_of_groups(5, 2))  # Output: 10
print(number_of_groups(6, 3))  # Output: 20