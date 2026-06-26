arr = [1, 1, 2, 2, 3, 3]


def count_frequencies(arr: list):
    my_dict = {}

    for number in arr:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1

    return my_dict


def find_max_frequency(arr: list):
    freq = count_frequencies(arr)
    max_freq = 0
    for key in freq:
        if freq[key] > max_freq:
            max_freq = freq[key]

    print(freq)
    print(max_freq)

    for key in freq:
        if freq[key] == max_freq:
            print(f"element with maximum frequency is: {key}")


find_max_frequency(arr)
