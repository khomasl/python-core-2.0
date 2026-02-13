is_nice = True
state = "nice" if is_nice else "not nice"
print("The weather is", state)

some_data = None
msg = some_data or "Не було повернено даних"
print(msg)