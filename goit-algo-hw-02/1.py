is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else:
    is_next = False

print("Is next? - ", is_next)
    
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)
print(a == b)
print(a == c)