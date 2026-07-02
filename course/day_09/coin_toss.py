def coin_toss(n: int, ans=""):
    if n == 0:
        print(ans)
        return
    # at every possible number
    # there are two outcomes.

    # first one is head
    coin_toss(n - 1, ans + "H")

    # second one is tails
    coin_toss(n - 1, ans + "T")


def binary_numbers(n: int, ans=""):
    if n == 0:
        print(ans)
        return
    binary_numbers(n - 1, ans + "0")
    binary_numbers(n - 1, ans + "1")


def dice_rolls(n: int, ans=""):
    if n == 0:
        print(ans)
        return
    for i in range(1, 7):
        dice_rolls(n - 1, ans + str(i))


def subseq(myStr: str, start_index=0, ans=""):
    if start_index == len(myStr):
        print(ans)
        return

    subseq(myStr, start_index + 1, ans + myStr[start_index])
    subseq(myStr, start_index + 1, ans)


subseq("abc", start_index=0, ans="")
