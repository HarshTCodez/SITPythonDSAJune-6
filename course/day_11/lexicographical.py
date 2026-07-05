def gen(n: int, k: int):
    if k > n:
        return

    print(k)
    for i in range(10):
        gen(n, 10 * k + i)


for i in range(1, 10):
    gen(200, i)
