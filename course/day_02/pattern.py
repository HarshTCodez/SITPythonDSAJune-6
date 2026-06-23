# Two right-angled triangles touching, meeting at the base.
# n = 2 ->            n = 3 ->
# * *                 *   *
# ***                 ** **
#                     *****

n = int(input("Enter N: "))

last_row_elements = n * 2 - 1
for i in range(1, n + 1):
    if i != n:
        current_row_elements = 2 * i
        number_of_gaps = last_row_elements - current_row_elements
        print("*" * i, end="")
        print(" " * number_of_gaps, end="")
        print("*" * i, end="")
        print()
    else:
        print("*" * last_row_elements)
