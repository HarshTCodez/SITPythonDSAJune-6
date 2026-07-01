def is_palindrome(s: str):
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(is_palindrome("abcdedbca"))
