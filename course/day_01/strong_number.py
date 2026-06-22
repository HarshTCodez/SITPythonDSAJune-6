# Strong number: a number whose sum of the factorial of its digits
# equals the number itself.  Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145

def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


n = int(input("n: "))
original_n = n

total = 0
while n > 0:
    digit = n % 10
    total += factorial(digit)
    n = n // 10

if total == original_n:
    print("It's a strong number")
else:
    print("It is not a strong number")
