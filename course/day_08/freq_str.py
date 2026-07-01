def get_freq_map(s: str):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1

    return freq


print(get_freq_map("abcdddeasdbc"))
