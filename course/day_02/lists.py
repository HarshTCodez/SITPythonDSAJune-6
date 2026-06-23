def finding_minimum(my_list):
    ans = float("inf")
    for x in my_list:
        if x < ans:
            ans = x
    return ans


def finding_maximum(my_list):
    ans = float("-inf")
    for x in my_list:
        if x > ans:
            ans = x
    return ans


def find_max_and_min(my_list):
    ans_max = float("-inf")
    ans_min = float("inf")

    for x in my_list:
        if x > ans_max:
            ans_max = x
        if x < ans_min:
            ans_min = x

    return [ans_min, ans_max]


def find_element(my_list, element):
    for i in range(len(my_list)):
        if my_list[i] == element:
            return i
    return -1


def print_reverse(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        print(my_list[i])


print(find_max_and_min([-2, -1, -4, -5, 0, 1, 2, 3, 4]))
