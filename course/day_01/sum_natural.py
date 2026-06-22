# Sum of all natural numbers till n.

n = int(input("n: "))

total = 0
for i in range(1, n + 1):
    total += i

print(total)

# Direct formula (no loop): n * (n + 1) // 2
print(n * (n + 1) // 2)
