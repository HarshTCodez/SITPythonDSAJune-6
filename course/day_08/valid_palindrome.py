class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char

        new_str = new_str.lower()
        return new_str == new_str[::-1]
