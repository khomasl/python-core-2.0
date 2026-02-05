while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break

while True:
    number = input("number = ")
    number = int(number)
    is_break = False
    while True:
        print(number)
        number = number - 1
        if number < 0:
            is_break = True
            break
    if is_break:
        break

