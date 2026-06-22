# Pattern printing - run any function to see it.

def left_triangle(n):
    # *
    # **
    # ***
    for i in range(1, n + 1):
        print("*" * i)


def inverted_left_triangle(n):
    # ***
    # **
    # *
    for i in range(n, 0, -1):
        print("*" * i)


def right_triangle(n):
    #   *
    #  **
    # ***
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


def pyramid(n):
    #   *
    #  ***
    # *****
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def rhombus(n):
    #   *
    #  ***
    # *****
    #  ***
    #   *
    for i in range(1, n + 1):                 # top half (with middle row)
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):             # bottom half
        print(" " * (n - i) + "*" * (2 * i - 1))


def hollow_rectangle(n, m):
    # n rows, m columns, only the border is *
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    n = int(input("n: "))
    print("\nleft_triangle"); left_triangle(n)
    print("\ninverted_left_triangle"); inverted_left_triangle(n)
    print("\nright_triangle"); right_triangle(n)
    print("\npyramid"); pyramid(n)
    print("\nrhombus"); rhombus(n)
    print("\nhollow_rectangle"); hollow_rectangle(n, n)
