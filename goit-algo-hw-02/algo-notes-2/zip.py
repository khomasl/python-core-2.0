list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат", "juice"]
for number, letter in zip(list1, list2):
    print(number, letter)

print(list(zip(list1, list2)))
