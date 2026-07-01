class Solution:
    def reverseWords(self, s: str) -> str:
        # my name is anmol
        # ["my", name, is, anmol]
        words = s.split()
        # [1,2,3,4]
        # [4, 3, 2, 1] list[::-1]
        reverse_words = words[::-1]
        # [anmol, is, name, my]
        return " ".join(reverse_words)
