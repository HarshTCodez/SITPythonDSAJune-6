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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for word in strs:
            # sorted_word = convert_freq_arr_to_str(get_freq_arr(word))
            sorted_word = "".join(sorted(word))

            if sorted_word not in hash:
                hash[sorted_word] = [word]
            else:
                hash[sorted_word].append(word)

        return list(hash.values())
