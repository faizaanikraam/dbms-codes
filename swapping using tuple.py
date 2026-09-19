x = 5
y = 7

print("Before swapping:", x, y)
x, y = 5, 7

print("Before swapping:", x, y)

# Swapping using tuple unpacking
x, y = y, x
# Swapping using arithmetic operations
x = x + y
y = x - y
x = x - y

print("After swapping:", x, y)