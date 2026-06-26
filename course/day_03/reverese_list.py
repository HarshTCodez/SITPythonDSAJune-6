x = [1, 2, 3, 4, 5, 6]


for i in range(0, len(x) // 2):
    last_element_index = len(x) - i - 1
    x[i], x[last_element_index] = x[last_element_index], x[i]


print(x)
