def count_bits(n: int):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count


#
# def count_bits(n: int):
#     count = 0
#     while n > 0:
#         n = n >> 1
#         count += 1
#     return count


print(count_bits(7))
print(count_bits(8))
print(count_bits(15))
print(count_bits(16))
