def a():
    print("entering a")
    print("exiting a")


def b():
    print("entering b")
    a()
    print("exiting b")


def c():
    print("entering c")
    b()
    print("exiting c")


def main():
    print("entering main")
    c()
    print("exiting main")


main()
print("after main")
