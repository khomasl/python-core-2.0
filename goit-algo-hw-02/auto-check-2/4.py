num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0:
    sum += num
    num -= 1
    
    
print("The sum of integers from 0 to the entered number is: ", sum)