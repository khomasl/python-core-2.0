for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')
