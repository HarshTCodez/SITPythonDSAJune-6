def get_freq_arr(s: str):
    res = [0] * 26

    for ch in s:
        number = ord(ch) - ord("a")
        res[number] += 1

    return res


def convert_freq_arr_to_str(res: list):
    ans = ""
    for i in range(26):
        if res[i] > 0:
            current_char = chr(i + ord("a"))
            ans += current_char * res[i]
    return ans


def is_anagram(s: str, t: str):
    if len(s) != len(t):
        return False

    freq1 = get_freq_arr(s)
    freq2 = get_freq_arr(t)

    if freq1 == freq2:
        return True
    else:
        return False


og_string = "abbacdeeafzz"
print(og_string)
freq1 = get_freq_arr(og_string)
print(freq1)

str1 = convert_freq_arr_to_str(freq1)
print(str1)
