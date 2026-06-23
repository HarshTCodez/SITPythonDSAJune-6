def a():
    print("function a was called")
    return 5


def b():
    print("function b pre")
    ans = a() + 1
    print("function b post")
    return ans


def c():
    print("function c pre")
    ans = b() + 1
    print("function c post")
    return ans


def d():
    print("function d pre")
    ans = c() + 1
    print("function d post")
    return ans


def main():
    ans = d()
    print(ans)


main()
