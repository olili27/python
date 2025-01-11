from cs50 import get_int

height: int = get_int("Height: ")

while (height <= 0) or height > 8:
    height: int = get_int("Height: ")
    
for i in range(1, height + 1):
    spaces = " " * (height - i)
    hush = "#" * i
    print(f"{spaces}{hush}", end="  ")
    print(f"{hush}")

