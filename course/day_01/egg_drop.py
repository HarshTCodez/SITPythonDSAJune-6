# Egg drop - 2 eggs, 100 floors, find the highest "safe" floor.
# Strategy: drop the FIRST egg every sqrt(n) floors.
# When it breaks, use the SECOND egg to go up one floor at a time
# from the last safe floor.

from math import floor, sqrt

floors = 100
step = floor(sqrt(floors))  # 10 -> drop first egg at 10, 20, 30, ...

first_egg_drops = list(range(step, floors + 1, step))
print("First egg dropped at floors:", first_egg_drops)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Worst case number of drops:
#   first egg  -> floors // step      = 10 jumps
#   second egg -> step - 1            = 9 single steps
worst_case = floors // step + (step - 1)
print("Worst case drops:", worst_case)  # 19
