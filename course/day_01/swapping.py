# Swapping two numbers - 4 ways.

a, b = 5, 9

# Method 1: using an extra (temp) variable
temp = a
a = b
b = temp
print(a, b)  # 9 5

# --- without an extra variable ---

a, b = 5, 9

# Method 2: arithmetic (+ / -)
a = a + b   # a = 14
b = a - b   # b = 14 - 9 = 5
a = a - b   # a = 14 - 5 = 9
print(a, b)  # 9 5

a, b = 5, 9

# Method 3: XOR (bitwise)
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 9 5

a, b = 5, 9

# Method 4: tuple unpacking (the Pythonic way)
a, b = b, a
print(a, b)  # 9 5
