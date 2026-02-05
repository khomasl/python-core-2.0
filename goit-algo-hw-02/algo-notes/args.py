def concatenate(*args) -> str:
    print(args)
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))
