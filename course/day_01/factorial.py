# Factorial of n  ->  n! = 1 * 2 * 3 * ... * n

n = int(input("n: "))

ans = 1
for i in range(1, n + 1):
    ans = ans * i

print(ans)
